from core.ollama_client import query_ollama


def review_diff(diff: str):
    issues = []

    if "print(" in diff:
        issues.append("Remove debug print statements")

    if "except:" in diff:
        issues.append("Avoid bare except")

    prompt = f"""
You are a senior Python engineer.

Review this diff and give issues:

{diff}
"""

    ai_review = query_ollama(prompt)

    return issues, ai_review
