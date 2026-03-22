from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import generate_draft

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/draft")
def draft(facts: str):
    result = generate_draft(facts)
    return {"draft": result}
