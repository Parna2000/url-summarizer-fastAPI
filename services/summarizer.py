import requests


async def summarize_website(url: str) -> str:
    try:
        # Request summary from SummarizeBot API
        response = requests.get(f"https://api.smmry.com/&SM_API_KEY=3B93824D73&SM_URL={url}")
        response.raise_for_status()
        summary = response.json().get("sm_api_content", "")
        return summary
    except Exception as e:
        raise e
