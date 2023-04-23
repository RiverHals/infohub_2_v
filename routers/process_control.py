from fastapi import APIRouter
import sys
import os
import subprocess
import psutil
sys.path.append(".")
from model import Process

router = APIRouter()

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


@router.post("/api/pn/start")
async def start_process(process: Process):
    # command = process.name
    if is_process_running(process):
        return {"status": "already running"}

    try:
        with open("output.txt", "w") as f:
            subprocess.Popen(process.name, shell=True, stdout=f, stderr=f, stdin=subprocess.PIPE)
            return {"status": "started"}
    except:
        return {"status": "failed to start"}


@router.post("/api/pn/stop")
async def stop_process(process: Process):
    pid = get_pid(process)
    if pid is None:
        return {"status": "not running"}

    try:
        process = psutil.Process(pid)
        process.terminate()
        return {"status": "stopped"}
    except:
        return {"status": "failed to stop"}