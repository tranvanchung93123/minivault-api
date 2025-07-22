# MiniVault API

A lightweight local REST API that simulates a core ModelVault feature: running a local LLM to respond to a user prompt — completely offline.

## Features

- Exposes a `POST /generate` endpoint
- Returns a stubbed response
- Logs all requests/responses to `logs/log.jsonl`

## Setup Instructions

1. **Clone the repository**
2. **Create a virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Run the API**
   ```
   uvicorn app.main:app --reload
   ```
5. **Test the endpoint**
   ```
   curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d "{\"prompt\": \"Hello, who are you?\"}"
   ```

## Notes

- All prompt/response pairs are logged to `logs/log.jsonl`.
- The response is currently stubbed for demonstration.

## Tradeoffs & Improvements

- **Stubbed Response:** The `/generate` endpoint currently returns a fixed response. For a real LLM, integrate a local model (e.g., Hugging Face Transformers).
- **Logging:** All requests and responses are logged with timestamps for traceability.
- **Error Handling:** Basic error handling is present; can be extended for robustness.
- **Docker:** Ensures reproducibility and easy deployment.
- **CLI:** Simplifies local testing and developer experience.
