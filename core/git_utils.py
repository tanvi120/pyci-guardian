import subprocess


def get_git_diff(base_branch="master"):
    try:
        committed = subprocess.run(
            ["git", "diff", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        ).stdout

        staged = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True
        ).stdout

        unstaged = subprocess.run(
            ["git", "diff"],
            capture_output=True,
            text=True
        ).stdout

        return committed + staged + unstaged

    except Exception as e:
        print("Git diff error:", e)
        return ""


def create_fix_branch(branch_name="fix/auto-fix"):
    try:
        subprocess.run(["git", "checkout", "-b", branch_name])
    except Exception as e:
        print("Branch creation failed:", e)
