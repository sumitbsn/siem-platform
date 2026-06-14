import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "gpt-oss:20b"


def ask_llm(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    if response.status_code != 200:
        raise Exception(
            f"Ollama Error: {response.status_code} - {response.text}"
        )

    result = response.json()

    return result["response"]