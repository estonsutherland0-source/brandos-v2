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
    return {"status": "BrandOS AI is running 🚀"}

@app.post("/analyze")
def analyze(request: BrandRequest):
    try:
        brand = request.brand_name

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Analyze this brand: {brand}

Give:
- 5 weaknesses
- 5 opportunities
- 3 business ideas
- revenue strategy
- score out of 100
"""
                }
            ]
        )

        return {
            "brand": brand,
            "analysis": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "error": str(e)
        }
