import subprocess


def get_git_diff(base_branch="main"):
    try:
        result = subprocess.run(
            ["git", "diff", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        print("Git diff error:", e)
        return ""


def create_fix_branch(branch_name="fix/auto-fix"):
    subprocess.run(["git", "checkout", "-b", branch_name])
