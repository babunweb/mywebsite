from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style='color:blue;'>🔥 Welcome to my website</h1>
    <p>This is my first website 🚀</p>

    <button onclick="alert('Hello da 😎')">Click Me</button>
    """
@app.route("/about")
def about():
    return "<h2>This is About Page 😎</h2>"
