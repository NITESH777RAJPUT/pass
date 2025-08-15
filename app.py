from flask import Flask, request, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

@app.route("/generate", methods=["POST"])
def generate_password():
    data = request.json
    length = data.get("length", 12)
    include_letters = data.get("letters", True)
    include_numbers = data.get("numbers", True)
    include_symbols = data.get("symbols", True)
    exclude_chars = data.get("exclude", "")

    chars = ""
    if include_letters:
        chars += string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    # Remove excluded characters
    if exclude_chars:
        chars = "".join(c for c in chars if c not in exclude_chars)

    if not chars:
        return jsonify({"error": "No character set selected"}), 400

    password = "".join(random.choice(chars) for _ in range(length))
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
