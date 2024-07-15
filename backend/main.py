from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/time")
def read_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}