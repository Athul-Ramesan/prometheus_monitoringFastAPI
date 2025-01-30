from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:str=None):
    return {"item_id":item_id, "q":q}

Instrumentator().instrument(app).expose(app)
