def build_prompt(brand_name, search_results, website_text):
    return f"""
You are a senior business analyst.

Analyze the brand: {brand_name}

SEARCH DATA:
{search_results}

WEBSITE DATA:
{website_text}

TASK:

1. List 5 weaknesses
2. List 5 missed opportunities
3. List 3 market gaps

Then generate 3 business opportunities:

For each:
- Idea name
- Explanation
- Target audience
- Monetization
- Step-by-step execution

Be very specific and avoid generic advice.
"""
