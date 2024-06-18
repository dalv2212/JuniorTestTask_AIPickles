# **Junior Python Developer test task**
## **Description**
A simple web application that integrates an AI-based text summarization service using
FastAPI and LangChain. The application must accept text input from the user and return a summarized 
summarized version of the text.
## **Instructions:**
### 1. Clone the repository:
      git clone [url]
### 2. Create a virtual environment:
      python -m venv env
      source env/bin/activate`  # On Windows use env\Scripts\activate
### 3. Create file .env:
* register your OPENAI_API_KEY= to access OpenAI

_*see for example the file .env.sample_
### 4. Set dependencies:
      pip install -r requirements.txt
### 5. Launch the app:
      uvicorn main:app --reload
### 6. Check the endpoint:
* Send a request POST http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.

_*example of the request (replace "Your text" with the desired one):_

`curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Your text"
}'`