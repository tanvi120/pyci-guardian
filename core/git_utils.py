import subprocess


def get_git_diff():
    try:
        committed = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True,
            text=True
        ).stdout

        unstaged = subprocess.run(
            ["git", "diff"],
            capture_output=True,
            text=True
        ).stdout

        return committed + unstaged

    except Exception as e:
        print("Git diff error:", e)
        return ""


def create_fix_branch(branch_name="fix/auto-fix"):
    try:
        subprocess.run(["git", "checkout", "-b", branch_name])
        print(f"✅ Created branch: {branch_name}")
    except Exception as e:
        print("❌ Branch creation failed:", e)
