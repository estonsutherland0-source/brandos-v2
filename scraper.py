import requests
from bs4 import BeautifulSoup

def search_brand(brand_name):
    try:
        url = f"https://www.google.com/search?q={brand_name}"
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        results = soup.find_all("h3")
        return [r.get_text() for r in results[:5]]

    except:
        return ["No search data found"]

def get_website_text(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text[:3000] if text else "No website content found"

    except:
        return "Website not reachable"
