from fastapi import APIRouter
import sys
import subprocess
import psutil
sys.path.append(".")
from model import Process
from routers.lib import get_pid


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
@router.get("/api/pn/result")
async def show_process_output(process: Process):
    pid = get_pid(process)
    if pid is None:
        return {"status": "process not found"}

    try:
        with open("output.txt", "r") as f:
            output = f.read()
        return {"output": output}
    except:
        return {"status": "failed to get output"}