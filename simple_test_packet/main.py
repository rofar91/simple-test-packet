from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: Optional[str] = None):
    return {"Hello": name}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("simple_test_packet.main:app", host="0.0.0.0", port=8000, reload=True)
