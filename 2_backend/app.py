"""
app.py

FastAPI main backend application for AI CaseFiles system.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI CaseFiles Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
