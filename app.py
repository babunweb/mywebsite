from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Idhu en first website 🔥"

if __name__ == '__main__':
    app.run(debug=True)