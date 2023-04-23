from fastapi import APIRouter
import psutil
from ..model import Process
from ..lib import get_pid

router = APIRouter()
@router.get("api/pn/result")
def show_process_output(process: Process):
    pid = get_pid(process)
    if pid is None:
        return {"status": "process not found"}

    try:
        process = psutil.Process(pid)
        output, _ = process.communicate()
        return {"output": output.decode("utf-8")}
    except:
        return {"status": "failed to get output"}