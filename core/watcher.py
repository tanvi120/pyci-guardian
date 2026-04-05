import time
from core.pipeline import run_pipeline
from core.git_monitor import get_latest_commit, has_new_commit

def start_watcher():
    print("👀 Watcher started...")

    prev_commit = get_latest_commit()

    while True:
        try:
            changed, new_commit = has_new_commit(prev_commit)

            if changed:
                print("🔄 Change detected, running pipeline...")
                run_pipeline()
                prev_commit = new_commit

        except Exception as e:
            print(f"Watcher error: {e}")

        time.sleep(10)
