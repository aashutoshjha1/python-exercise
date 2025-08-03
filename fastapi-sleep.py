#!/usr/bin/env python3

from fastapi import FastAPI
from time import sleep
import asyncio

app = FastAPI()


@app.get("/sys_sleep")
def sys_sleep():
    sleep(1)
    return {"message": None}

@app.get("/aio_sleep")
async def aio_sleep():
    sleep(1)
    return {"message": None}


@app.get("/aio_await_sleep")
async def aio_await_sleep():
    await asyncio.sleep(1)
    return {"message": None}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
