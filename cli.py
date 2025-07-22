import requests
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py 'your prompt here'")
        return
    prompt = sys.argv[1]
    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={"prompt": prompt}
    )
    print("Response:", response.json()["response"])

if __name__ == "__main__":
    main()