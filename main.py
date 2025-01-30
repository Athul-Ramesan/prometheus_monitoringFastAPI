from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge, make_asgi_app
from fastapi.responses import JSONResponse
import random

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

#Define prometheus metrics
REQUEST_COUNTER = Counter(
    "app_requests_total", #metric name
    "Total number of requests to the app", #metric description
    ["endpoint"], #Labels (e.g endpoint names)
)

RANDOM_NUMBER_GAUGE = Gauge(
    "app_random_number", #metric name
    "current value of the random number", #metric description
)


@app.get("/", response_class=JSONResponse)
def get_homepage():
    #increment the request counter
    REQUEST_COUNTER.labels(endpoint="/").inc()

    random_number = random.randint(a=0,b=100)
    print(random_number)
    RANDOM_NUMBER_GAUGE.set(random_number)
    return {"status":"OK", "random_number":random_number}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:str=None):
    return {"item_id":item_id, "q":q}

Instrumentator().instrument(app).expose(app)
