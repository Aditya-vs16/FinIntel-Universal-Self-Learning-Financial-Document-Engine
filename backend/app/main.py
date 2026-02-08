from fastapi import FastAPI

# Create the backend application
app = FastAPI()

# Home route (just to check server is alive)
@app.get("/")
def home():
    return {
        "message": "FinIntel backend is running"
    }
