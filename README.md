# Lab 04 — Basic HTTP with Flask (GitHub Codespaces)

Small Flask service with three endpoints:

- `GET /` → returns the text `" you called "` (note the leading space + newline)
- `POST /echo` → echoes back whatever you send in the `text` field  
  Response format: `You said: <text>`
- `GET /factors?inINT=<n>` **and** `POST /factors` → returns a JSON list of factors per lab spec:  
  - if `n` is **prime** → `[n]`  
  - if `n` is **composite** → `[1] + <prime factors>` (e.g., `12` → `[1, 2, 2, 3]`)

---

## Project Structure
├── app.py
├── requirements.txt
├── tests/
│ └── test_app.py
└── README.md
1. Open this repo in **GitHub Codespaces**.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

# Run 
python app.py

# root
curl -s http://127.0.0.1:5000/

# echo
curl -s -X POST -d "text=Hello Ettory!" http://127.0.0.1:5000/echo

# factors (composite)
curl -s "http://127.0.0.1:5000/factors?inINT=12"

# factors (prime)
curl -s "http://127.0.0.1:5000/factors?inINT=13"
