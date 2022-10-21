from typing import Optional, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root(name: Optional[str] = None):
    return {"Hello": name}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None


@app.post("/name")
def create_item(item: Item):
    return item


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("simple_test_packet.main:app", host="0.0.0.0", port=8080, reload=True)
