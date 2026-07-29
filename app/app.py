from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/desafio")
def desafio():
    return render_template("desafio.html")


@app.route("/health")
def health():
    return render_template("health.html")


@app.route("/api/info")
def api_info():
    return jsonify(
        {
            "application": "Donde esta el Secret",
            "version": "1.0.0",
            "status": "running",
            "conference": "DojoConf"
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)