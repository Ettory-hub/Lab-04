import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return " you called \n"

@app.post("/echo")
def echo():
    text = request.form.get("text")
    if text is None and request.is_json:
        text = (request.get_json(silent=True) or {}).get("text")
    return f"You said: {text}" if text is not None else "You said: "

def _prime_factors(n: int):
    """Return prime factors (no 1). Requires n >= 2."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors

def _lab_spec_factors_list(n: int):
    """
    Matches lab spec:
      - if n is prime -> [n]
      - else -> [1] + prime factors
    """
    pfs = _prime_factors(n)
    if len(pfs) == 1 and pfs[0] == n:
        return [n]             
    return [1] + pfs            

@app.get("/factors")
def get_factors():
    raw = request.args.get("inINT", None)
    if raw is None:
        return jsonify(error="missing inINT"), 400
    try:
        n = int(raw)
    except ValueError:
        return jsonify(error="inINT must be an integer"), 400
    if n < 2:
        return jsonify(error="inINT must be >= 2"), 400

    return jsonify(input=n, factors=_lab_spec_factors_list(n))

@app.post("/factors")
def post_factors():
    # Accept JSON or form-encoded
    raw = None
    if request.is_json:
        raw = (request.get_json(silent=True) or {}).get("inINT")
    if raw is None:
        raw = request.form.get("inINT")

    if raw is None:
        return jsonify(error="missing inINT"), 400
    try:
        n = int(raw)
    except ValueError:
        return jsonify(error="inINT must be an integer"), 400
    if n < 2:
        return jsonify(error="inINT must be >= 2"), 400

    return jsonify(input=n, factors=_lab_spec_factors_list(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
