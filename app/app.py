from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    threats_list = [
        "Suspicious SSH Login",
        "Port Scan Detected",
        "Large Packet Traffic"
    ]
    return render_template("dashboard.html", threats=threats_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)