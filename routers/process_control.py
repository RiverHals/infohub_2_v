from fastapi import APIRouter
import subprocess
from ..model import Process

router = APIRouter()

@router.post("api/pn/start")
def start_process(process: Process):
    command = process.name
    if command.is_process_running():
        return {"status": "already running"}

    try:
        subprocess.Popen(["systemctl", "start", command])
        return {"status": "started"}
    except:
        return {"status": "failed to start"}


@router.post("api/pn/stop")
def stop_process(process: Process):
    command = process.name
    if not command.is_process_running():
        return {"status": "not running"}

    try:
        subprocess.Popen(["systemctl", "stop", command])
        return {"status": "stopped"}
    except:
        return {"status": "failed to stop"}