from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Idhu en first website 🔥"

# IMPORTANT FOR RAILWAY
port = int(os.environ.get("PORT", 8080))

app.run(host="0.0.0.0", port=port)
