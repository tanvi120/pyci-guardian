from core.ollama_client import query_ollama


def generate_fix(diff: str, error_log: str):
    prompt = f"""
You are an expert Python engineer.

The following code caused an error.

DIFF:
{diff}

ERROR:
{error_log}

Provide:
1. Root cause
2. Fixed code
3. Explanation
"""

    return query_ollama(prompt)
