
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/fleet")
def fleet():
    return [
        {"id":"TRUCK-201","status":"active","health":0.87},
        {"id":"EXC-88","status":"maintenance","health":0.42}
    ]

@app.get("/prediction/{equipment_id}")
def prediction(equipment_id:str):
    return {
        "equipment_id": equipment_id,
        "failure_probability": round(random.random(),2),
        "days_to_failure": random.randint(1,10)
    }
