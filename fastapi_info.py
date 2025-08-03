#!/usr/bin/env python3

from fastapi import FastAPI
from datetime import datetime, timezone
import json
import os

app = FastAPI()

@app.get('/info')

def info():
   user_info = {}
   user_info['version'] = '1.0.0'
   user_info['time'] = datetime.now(timezone.utc).isoformat()
   user_info['user'] = os.environ['USER']
   json_str = json.dumps(user_info)
   return {json_str}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
