from fastapi import FastAPI, Form, Request, Response, File, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import os
# import openai
import json
import time
import uvicorn
from langchain import OpenAI
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
import spacy
import numpy as np
from dotenv import load_dotenv
import warnings

warnings.filterwarnings('ignore')

load_dotenv()

nlp = spacy.load('en_core_web_md')

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def save_history_to_file(history):
    """
    Save the history of interactions to a file
    """
    with open("history.txt", "w+") as f:
        return f.write(history)

def load_history_from_file():
    """ 
    Load all the history of interactions from a file
    """
    with open("history.txt", "r") as f:
        return f.read()

def cos_sim(a, b):
    """ 
    Calculate cosine similarity between two strings
    Used to compare the similarity between the user input and a segments int the history
    """
    a = nlp(a)
    b = nlp(b)
    a_without_stopwords = nlp(' '.join([t.text for t in a if not t.is_stop]))
    b_without_stopwords = nlp(' '.join([t.text for t in b if not t.is_stop]))
    return a_without_stopwords.similarity(b_without_stopwords)

def sort_history(history, user_input):
    """ 
    Sort the history of interactions based on cosine similarity between the user input and the segements in
    the history
    History is a string of segments seperated by separator
    """
    segments = history.split(seperator)
    similarities = []
    
    for segment in segments:
        # get cosine similarity between user input and segment
        similarity = cos_sim(user_input, segment)
        similarities.append(similarity)
    sorted_similarities = np.argsort(similarities)
    sorted_history = ""
    for i in range(1, len(segments)):
        sorted_history += segments[sorted_similarities[i]] + seperator
    save_history_to_file(sorted_history)

def get_latest_n_from_history(history, n):
    """ 
    Get the latest n segments from the history
    History is a string of segments seperated by separator
    """
    segments = history.split(seperator)
    return seperator.join(segments[-n:])

initial_prompt_1 = """ 
You: Hi there!
AI: Hello!
#####
You: How are you?
AI: I am fine, thank you.
#####
You: Do you know cars?
AI: Yes I have some knowledge about cars.
#####
You: Do you eat Pizza?
AI: I don't eat Pizza. I am an AI that is not able to eat.
#####
You: Have you ever been to the moon?
Context & Memory: Making AI More Real 174
AI: I have never been to the moon. What about you>
#####
You: What is you name?
AI: My name is Pixel. What is your name?
#####
You: What is your favorite movie?
AI: My favorite movie is The Matrix. Follow the white rabbit :)
#####
"""
initial_prompt_2 = """You: {}
AI: """
initial_prompt = initial_prompt_1 + initial_prompt_2
seperator = "#####"

save_history_to_file(initial_prompt_1)

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 1024
    max_chunk_overlap = 20
    chunk_size_limit = 600
    
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit)
    
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003",
                                            max_tokens=num_outputs,
                                            stop=[" You:", " AI:"]))

    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    
    index.save_to_disk(index.json)
    
    return index

def qabot(input_text):
    start = time.time()
    print(input_text)
    prompt = input_text
    sort_history(load_history_from_file(), prompt)
    history = load_history_from_file()
    best_history = get_latest_n_from_history(history, 5)
    full_user_prompt = initial_prompt_2.format(prompt)
    print("full_user_prompt: ", full_user_prompt)
    full_prompt = best_history + "\n" + full_user_prompt
    print("full_prompt: ", full_prompt)
    
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(full_prompt, response_mode="compact")
    response_text = response.response.strip()
    print("AI: ",response_text)
    history += "\n" + full_user_prompt + response_text + "\n" + seperator + "\n"
    save_history_to_file(history)
    
    end = time.time()
    print("Time taken for generating response : :", round(end-start, 2))
    
    return response.response

index = construct_index("docs")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})