import torch
import torch.nn as nn
import math


class InputEmbeddings(nn.Module):
    def __init__(self, d_model:int, vocab_size:int):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, d_model)
    def forward(self, X):
        return self.embedding(X) * math.sqrt(self.d_model)

    
class PositionalEncoding(nn.Module):
    def __init__(self, d_model:int, seq_length:int, dropout:float):
        super().__init__()
        self.d_model = d_model
        self.seq_length = seq_length
        self.dropout = nn.Dropout(p = dropout)
            
        # create positional encoding matrix of size = seq_length * d_model
        pe = torch.zeros(self.seq_length, self.d_model)
        # create a vector of shape (seq_length, 1)
        position = torch.arange(0, seq_length, dtype=torch.float).unsqueeze(1)
        # the following div term is the derivation of the original div term in the paper
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        # applying sin and cosine to even and odd positins
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        # lets adjust it for batches
        # there would be multiple sentences passed at a same time
        pe = pe.unsqueeze(0) # (1, seq_len, d_model)
        self.register_buffer('pe', pe)
    
    def forward(self, X):
        X = X + (self.pe[:, :X.shape[1], :]).requires_grad_(False)
        return self.dropout(X)

class LayerNormalization(nn.Module):
    def __init__(self, eps:float = 1e-6):
        super().__init__()
        self.eps = eps
        self.alpha = nn.Parameter(torch.ones(1)) # Multiplied
        self.bias = nn.Parameter(torch.zeros(1)) # Added
    def forward(self, X):
        mean = X.mean(dim=-1, keepdim=True)
        std = X.std(dim=-1, keepdim=True)
        return self.alpha * (X - mean) / (std + self.eps) + self.bias

class FeedForwardBlock(nn.Module):
    """
    Normal Feed Forward Network with 3 args.

    Args:
        d_model: This is the dimensinality of input features. Also, the dimensionality
            of the model.
        d_ff: Size of the hidden layer. Usally 4x bigger than d_model.
        dropout: This is prob. value to determine how much neurons to "drop" during
            training to prevent overfitting.
    """
    def __init__(self, d_model:int, d_ff:int, dropout:float):
        super().__init__()
        self.linear_1 = nn.Linear(d_model, d_ff)
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(d_ff, d_model)
    def forward(self, X):
        #(Batch size, seq len, d_model) -> (Batch size, seq len, d_ff) -> (Batch size, seq len, d_model)
        X = self.dropout(nn.ReLU(self.linear_1(X)))
        logits = self.linear_2(X)
        return logits

        
class MultiHeadAttentionBlock(nn.Module):
    def __init__(self, d_model:int, h:int, dropout:float):
        super().__init__()
        self.d_model = d_model
        self.h = h
        assert d_model%h == 0, "d_model is not divisible by h"
        #d_k is a divison of Q matrix
        self.d_k = d_model // h
        # weight matrix = (d_model, d_model)
        self.w_q = nn.Linear(d_model, d_model) # Wq = weights of query matrix
        self.w_k = nn.Linear(d_model, d_model) # Wk
        self.w_v = nn.Linear(d_model, d_model) # Wv

        self.w_o = nn.Linear(d_model, d_model) # Wo
        self.dropout = nn.Dropout(dropout)

    @staticmethod
    def attention(query, key, value, mask, dropout:nn.Dropout):
        d_k = query.shape[-1]

        # (batch, h, seq_len, d_k) -> (batch, h, seq_len, seq_len)
        attention_scores = (query @ key.transpose(-2, -1)) / math.sqrt(d_k)
        if mask is not None:
            attention_scores.mased_fill_(mask==0, 1e-9)
        attention_scores = attention_scores.softmax(dim -1) # (batch, h, seq_len, seq_len)
        if dropout is not None:
            attention_scores = dropout(attention_scores)
        
        return (attention_scores @ value), attention_scores
    
    def forward(self, q, k, v, mask):
        # in the following opearions dimensions : (Batch, seq len, d_model) * (Batch, d_model, d_model)
        # -> (Batch, seq len, d_model) 
        query = self.w_q(q)
        key = self.w_k(k)
        value = self.w_v(v)

        # now we will divide query,key,value into smaller matrices
        # this will be done torch.view (3d->4d matrice)
        # original shape = (batch, seq_len, d_model)
        # transformed shape = (batch, seq_len, h, Dk) # d_model = h*Dk
        # transposed shape = (batch, h, seq_len, Dk)
        query = query.view(query.shape[0], query.shape[1], self.h, self.d_k).transpose(1,2)
        key = key.view(key.shape[0], key.shape[1], self.h, self.d_k).transpose(1,2)
        value = value.view(value.shape[0], value.shape[1], self.h, self.d_k).transpose(1,2)

        X, self.attention_scores = MultiHeadAttentionBlock.attention(query, key, value, mask, self.dropout)

        # (Batch, h, seq_len, dk) -> (batch, seq_len, h, dk) -> (batch, seq_len, d_model)
        X = X.transpose(1,2).contiguous().view(X.shape[0], -1, self.h * self.d_k)

        return self.w_o(X)

        
class ResidualConnection(nn.Module):
    def __init__(self, dropout:float):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        self.norm = LayerNormalization()

    def forward(self, X, sublayer):
        return X + self.dropout(sublayer(self.norm(X)))

        
class EncoderBlock(nn.Module):
    def __init__(self,
                 self_attention_block:MultiHeadAttentionBlock,
                 feed_forward_block:FeedForwardBlock,
                 dropout:float):
        self.self_attention_block = self_attention_block
        self.feed_forward_block = feed_forward_block
        self.residual_connections = nn.ModuleList([ResidualConnection(dropout) for _ in range(2)])

    def forward(self, X, src_mask):
        X = self.residual_connections[0](X, lambda X:self.self_attention_block(X, X, X, src_mask))