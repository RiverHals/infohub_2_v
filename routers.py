from fastapi import FastAPI

from fastapi.responses import RedirectResponse
import subprocess
import main

app = FastAPI()

@app.post("api/pn/start")
def start_process():
    if main.is_process_running():
        return {"status": "already running"}

    try:
        subprocess.Popen(["systemctl", "start", process.name])
        return {"status": "started"}
    except:
        return {"status": "failed to start"}


@app.post("api/pn/stop")
def stop_process():
    if not main.is_process_running():
        return {"status": "not running"}

    try:
        subprocess.Popen(["systemctl", "stop", process.name])
        return {"status": "stopped"}
    except:
        return {"status": "failed to stop"}
@app.get("api/pn/status")
def status_process():
    if main.is_process_running():
        return {"status": "running"}
    else:
        return {"status": "not started"}


