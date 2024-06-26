from fastapi import FastAPI
from routers import summarize

app = FastAPI()

app.include_router(summarize.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the summarization API"}
