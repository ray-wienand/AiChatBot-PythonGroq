# Groq & Llama3 Chatbot
---

Simple Groq & Llama3 project to demonstrate using Python, Llama3 and Groq Cloud API.

## Tech Stack

- [GroqCloud](https://console.groq.com/login) Create Groq Cloud API.
- [Llama3](https://llama.meta.com/llama3/)
- Python v3.9.13
---

## Setup Instructions

### Update .env-example file
- Change the name from .env-example to .env
- Update the .env file with your GROQ_API_KEY

### Setup a virtual environment

`python3 -m venv env`

### Load virtual environment (Mac)

`source env/bin/activate`

### Install dependencies

`pip install -r requirements.txt`

### Run Basic Call
basic_call.py is a file to test that the connect with the groq api and Llama3 works.\

__Run__: `python basic_call.py`

### Run Chatbot
`streamlit run chatbot.py`

### Bonus Features
- Streamlit for a visual experience
- A memory of the last 10 conversations
- Sarcasm

