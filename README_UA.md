# **Тестове завдання Junior Python Developer**
## **Опис**
Проста веб-програма, яка інтегрує службу підсумовування тексту на основі ШІ за допомогою
FastAPI та LangChain. Додаток має прийняти текстове введення від користувача та повернути узагальнену 
версію тексту.
## **Інструкція:**
### 1. Склонувати репозиторій:
      git clone [url]
### 2. Створіть віртуальне середовище:
      python -m venv env
      source env/bin/activate  # On Windows use env\Scripts\activate
### 3. Створити файл .env:
* прописати параметр OPENAI_API_KEY= для доступу до OpenAI

_*дивитись для прикладу файл .env.sample_
### 4. Встановити залежності:
      pip install -r requirements.txt
### 5. Запустіть додаток:
      uvicorn main:app --reload
### 6. Перевірте кінцеву точку:
* Надішліть запит POST http://127.0.0.1:8000/summarize із тілом JSON, що містить текст, який потрібно підсумувати.

_*приклад запиту (замінити "Ваш текст" на бажаний текст):_

`curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Ваш текст"
}'`