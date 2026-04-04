import subprocess


def get_git_diff(base_branch="main"):
    try:
        # 1. committed diff
        committed = subprocess.run(
            ["git", "diff", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        ).stdout

        # 2. staged diff
        staged = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True
        ).stdout

        # 3. unstaged diff (WORKING DIR)
        unstaged = subprocess.run(
            ["git", "diff"],
            capture_output=True,
            text=True
        ).stdout

        full_diff = committed + staged + unstaged

        return full_diff

    except Exception as e:
        print("Git diff error:", e)
        return ""
