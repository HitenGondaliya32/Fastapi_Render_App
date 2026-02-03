from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI from Render 🚀"}

@app.get("/health")
def health_check():
    return {"status": "OK"}
