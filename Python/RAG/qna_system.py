from sentence_transformers import SentenceTransformer
import cohere
import psycopg2
import streamlit as st
from psycopg2.extensions import register_adapter, AsIs
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Sentence transformer setup
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# PostgreSQL connection
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB_NAME"),
    user=os.getenv("POSTGRES_DB_USER"),
    password=os.getenv("POSTGRES_DB_PASSWORD"),
    host=os.getenv("POSTGRES_DB_HOST"),
    port=os.getenv("POSTGRES_DB_PORT"),
)
cursor = conn.cursor()

# Create database table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS document_chunk2(
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding vector(384)  -- MiniLM-L6-v2 produces 384-dimensional embeddings
    );
""")
conn.commit()

# Reading document
with open('ai.txt', 'r', encoding='utf-8') as f:
    document = f.read().splitlines()

st.title("Interactive Q&A System with RAG")

# Generate and store embeddings in PostgreSQL
st.header("Generating Embeddings")
for i, doc in enumerate(document):
    embedding = sentence_model.encode(doc).flatten().tolist()
    cursor.execute("""
    INSERT INTO document_chunk2(content, embedding) 
    VALUES (%s, %s)
    """, (doc, embedding))
    if i == 1 or i == 2:
        st.write(f"Embedding for : {doc} -> {embedding}")
conn.commit()

# Retrieving relevant chunks for the question
st.header("Retrieving Relevant Chunks for the Question")
question = st.text_input("Enter your Question:")

def get_relevant_chunks(question, top_n=3):
    question_embedding = sentence_model.encode(question).flatten().tolist()
    cursor.execute("""
                   SELECT content
                   FROM document_chunk2
                   ORDER BY embedding <=> %s::vector
                   LIMIT %s
                   """, (question_embedding, top_n))
    relevant_chunks = [row[0] for row in cursor.fetchall()]
    return relevant_chunks

if question:
    st.write(f"**Embedding for the question** {question}")
    question_embedding = sentence_model.encode(question).flatten().tolist()
    st.write(question_embedding)

    relevant_chunks = get_relevant_chunks(question)
    st.write("Top relevant chunks retrieved: ")
    for i, chunk in enumerate(relevant_chunks, start=1):
        st.write(f"{i} -> {chunk}")

    # Generate the answer using LLaMA
    st.header("Generate Answer using LLaMA")
    context = "\n".join(f"{i+1}. {chunk}" for i, chunk in enumerate(relevant_chunks))
    prompt = f"Using the following information:\n{context}\nAnswer the question: {question}"

    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=100,
        temperature=0.3
    )
    answer = response.generations[0].text
    st.write("Answer:", answer)

cursor.close()
conn.close()