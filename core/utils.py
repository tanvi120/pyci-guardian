import re

def extract_file_from_diff(diff: str):
    """
    Extract first changed file path from git diff
    """
    match = re.search(r"diff --git a/(.*?) b/", diff)
    if match:
        return match.group(1)
    return None
