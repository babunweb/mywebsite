from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style='color:red;'>🔥 Welcome to my website</h1>
    <p>This is my first website 🚀</p>

    <button onclick="alert('Hello da 😎')">Click Me</button>
    """
    
