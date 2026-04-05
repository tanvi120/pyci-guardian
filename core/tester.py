import subprocess


def run_tests():
    result = subprocess.run(
        ["python3", "-m", "pytest"],
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "output": result.stdout + result.stderr
    }
