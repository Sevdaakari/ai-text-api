import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import HTTPException
from google.genai import errors


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is my API."}

class TextRequest(BaseModel):
    text: str

@app.post("/echo")
def echo_text(request: TextRequest):
    return {"you_sent": request.text}  


@app.post("/summarize")
def summarize_text(request: TextRequest):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"Summarize this text in one sentence: {request.text}")
        return {"summary": response.text}
    except errors.ClientError as e:
        print("ACTUAL ERROR:", e)
        raise HTTPException(status_code=503, detail="AI service is temporarily unavailable. Please try again shortly.")

@app.post("/translate")
def translate_text(request: TextRequest):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"Translate the following text to Azerbaijani. Return ONLY the translated text, with no explanation, no extra commentary, and no markdown formatting: {request.text}")
        return {"translation": response.text}
    except errors.ClientError as e:
        print("ACTUAL ERROR:", e)
        raise HTTPException(status_code=503, detail="AI service is temporarily unavailable. Please try again shortly.")
@app.get("/app", response_class=FileResponse)
def serve_frontend():
    return "static/index.html"

app.mount("/static", StaticFiles(directory="static"), name="static")