#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    new = dict()
    new["age"] = 34
    new["name"] = "aashutosh"

    return {"message": new}

@app.get('/hello')

def hello():
  return {"message": "hello world"}

if __name__== '__main__':
    import uvicorn
    uvicorn.run(app)


