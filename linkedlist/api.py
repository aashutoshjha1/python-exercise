from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from log_scraper import scrape_logs
import os

app = FastAPI()

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "example.log")  # Change as needed

@app.get("/logs")
def get_logs(pattern: str = Query(None), since: str = Query(None)):
    """
    API endpoint to fetch logs. Optional query params:
    - pattern: regex to filter log lines
    - since: ISO datetime string to filter logs after this time
    """
    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid 'since' datetime format. Use ISO format.")
    logs = scrape_logs(LOG_FILE_PATH, pattern=pattern, since=since_dt)
    return {"logs": logs}
