import subprocess
import psutil
from model import Process


def get_pid(process: Process):
    try:
        pid = subprocess.check_output(["pgrep", process.name])
        return int(pid)
    except:
        return None


def is_process_running(process: Process):
    pid = get_pid()
    if pid is None:
        return False

    try:
        process = psutil.Process(pid)
        if process.status() == psutil.STATUS_RUNNING:
            return True
    except:
        return False

    return False


