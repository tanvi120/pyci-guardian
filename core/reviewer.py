from core.ollama_client import query_ollama


def review_diff(diff: str):
    issues = []

    # Rule-based checks
    if "SELECT *" in diff:
        issues.append("Avoid SELECT * in queries")

    if "print(" in diff:
        issues.append("Remove debug print statements")

    if "except:" in diff:
        issues.append("Avoid bare except")

    # AI Review
    prompt = f"""
You are a senior Python/data engineer.

Review this git diff:

{diff}

Give:
- Bugs
- Code smells
- Improvements
(Keep it short)
"""

    ai_review = query_ollama(prompt)

    return issues, ai_review
