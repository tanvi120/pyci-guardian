import re
from core.ollama_client import query_ollama


def extract_code_block(text: str):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def generate_fix(diff: str, error_log: str):
    prompt = f"""
Fix the broken Python code.

Return ONLY code inside ```python``` block.

DIFF:
{diff}

ERROR:
{error_log}
"""

    response = query_ollama(prompt)
    code = extract_code_block(response)

    return code, response
