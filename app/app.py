from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "CI/CD Demo Application",
        "status": "running",
        "version": "3.0.4"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": "3.0.4"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
