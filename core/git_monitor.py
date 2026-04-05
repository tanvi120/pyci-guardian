import subprocess

def get_latest_commit():
    return subprocess.getoutput("git rev-parse HEAD")

def has_new_commit(prev_commit):
    current = get_latest_commit()
    return current != prev_commit, current
