from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Parking DEV environment is running 🚀"}from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Parking DEV environment is running 🚀"}
