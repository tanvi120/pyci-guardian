import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def query_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "")
    except Exception as e:
        return f"Ollama error: {str(e)}"
