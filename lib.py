import subprocess
import psutil

def get_pid():
    try:
        pid = subprocess.check_output(["pgrep", process.name])
        return int(pid)
    except:
        return None


def is_process_running():
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


