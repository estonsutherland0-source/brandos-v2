from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from analyzer import analyze_brand

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BrandRequest(BaseModel):
    brand_name: str

@app.post("/analyze")
def analyze(request: BrandRequest):
    return analyze_brand(request.brand_name)
