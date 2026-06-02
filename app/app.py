from flask import Flask, render_template

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
    app.run(debug=True)