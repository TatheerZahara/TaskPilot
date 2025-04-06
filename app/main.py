from fastapi import FastAPI

app = FastAPI(title="Vowly", description="AI Wedding Planner", version="1.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to AI wedding planning"}