from fastapi import APIRouter
import subprocess
import psutil
import sys
sys.path.append(".")
from model import Process

def get_pid(process: Process):
    try:
        pid = subprocess.check_output(["pgrep", process.name])
        return int(pid)
    except:
        return None
def is_process_running(process: Process):
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        if proc.info['name'] == "python":
            return True
    return False

router = APIRouter()
@router.get("/api/pn/")
async def status_process(process: Process):
    command = process.name
    if is_process_running(command):
        return {"status": "running"}
    else:
        return {"status": "not started"}