import os
import re
from datetime import datetime

def scrape_logs(log_file_path, pattern=None, since=None):
    """
    Scrape logs from a file, optionally filtering by regex pattern and/or datetime.
    Args:
        log_file_path (str): Path to the log file.
        pattern (str, optional): Regex pattern to filter log lines.
        since (datetime, optional): Only include logs after this datetime.
    Returns:
        list: List of log lines (strings) matching the criteria.
    """
    logs = []
    if not os.path.exists(log_file_path):
        return logs
    regex = re.compile(pattern) if pattern else None
    with open(log_file_path, 'r') as f:
        for line in f:
            if since:
                # Example: parse datetime from log line, adjust as per log format
                try:
                    log_time = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
                    if log_time < since:
                        continue
                except Exception:
                    pass
            if regex and not regex.search(line):
                continue
            logs.append(line.strip())
    return logs
