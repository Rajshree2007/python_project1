
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Python Website!</h1>
    <h2>Version1.0.0</h2>
    <p>Deployed successfully using Jenkins Freestyle.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
