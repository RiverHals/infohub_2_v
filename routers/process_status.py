from fastapi import APIRouter
from ..model import Process

router = APIRouter()
@router.get("api/pn/")
def status_process(process: Process):
    command = process.name
    if command.is_process_running():
        return {"status": "running"}
    else:
        return {"status": "not started"}