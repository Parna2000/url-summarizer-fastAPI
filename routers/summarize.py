from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, HttpUrl
from services.summarizer import summarize_website

router = APIRouter()


class SummarizeRequest(BaseModel):
    url: str


class SummarizeResponse(BaseModel):
    url: str
    summary: str


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    try:
        summary = await summarize_website(request.url)
        return SummarizeResponse(url=request.url, summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
