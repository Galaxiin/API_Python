from typing import Union
from fastapi import FastAPI

from Data import Item

app = FastAPI()

@app.get("/Wolrd")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)