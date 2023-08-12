# Q23. Write a function called word_count(text) that takes a string as input and returns a dictionary where
# Each key is a word in the text and its value is the number of times that word appears in the text.
# for example, word_count("hello world hello") should return {"hello": 2, "world": 1}

def word_count(text: str):
    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

text = 'hello world hello'
print(word_count(text))