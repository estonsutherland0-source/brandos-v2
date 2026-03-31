import openai
import os
from scraper import search_brand, get_website_text
from prompts import build_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_brand(brand_name):
    search_results = search_brand(brand_name)

    website_url = f"https://www.{brand_name.lower()}.com"
    website_text = get_website_text(website_url)

    prompt = build_prompt(brand_name, search_results, website_text)

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return {
        "brand": brand_name,
        "website": website_url,
        "search_results": search_results,
        "analysis": response.choices[0].message.content
    }
