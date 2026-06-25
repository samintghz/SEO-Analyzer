from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from analyzer import analyze_website


app = FastAPI(
    title="SEO Analyzer API",
    description="A simple SEO auditing tool",
    version="1.0"
)


# CORS تنظیمات
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WebsiteRequest(BaseModel):
    url: str
    keyword: str | None = None



@app.get("/")
def home():
    return {
        "message": "SEO Analyzer API is running"
    }



@app.post("/analyze")
def analyze(request: WebsiteRequest):

    result = analyze_website(
        request.url,
        request.keyword
)
    

    return result