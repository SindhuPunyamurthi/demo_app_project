from flask import Flask
import os

app = Flask(__name__)

PORT = os.getenv("APP_PORT")
if not PORT:
    raise RuntimeError("APP_PORT is not set")

@app.route("/")
def home():
    return {
        "app": "port-demo-app",
        "port": PORT
    }

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))

