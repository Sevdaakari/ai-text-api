# AI Text Toolkit

A simple API that summarizes or translates text using Google's Gemini AI, built with FastAPI.

## What it does

- Summarizes text into one sentence
- Translates text into Azerbaijani

## Tech used

- Python, FastAPI
- Google Gemini API (google-genai)
- Docker
- HTML/CSS/JavaScript for a simple frontend

## How to run it

1. Clone this repo
2. Create a `.env` file with your Gemini API key:

GEMINI_API_KEY=your_key_here

3. Build and run with Docker:

docker build -t ai-text-api .
docker run -p 8000:8000 --env-file .env ai-text-api

4. Open `http://127.0.0.1:8000/app` in your browser


## Notes

This is a learning project — error handling and prompt design could be improved further.