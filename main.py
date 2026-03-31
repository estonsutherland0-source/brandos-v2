from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BrandRequest(BaseModel):
    brand_name: str

@app.get("/")
def home():
    return {"status": "BrandOS AI Level 2 is running 🚀"}

@app.post("/analyze")
def analyze(request: BrandRequest):
    brand = request.brand_name

    prompt = f"""
    You are a business expert.
    Analyze: {brand}
    Give weaknesses, opportunities, ideas, and a score out of 100.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "brand": brand,
        "analysis": response.choices[0].message.content
    }
