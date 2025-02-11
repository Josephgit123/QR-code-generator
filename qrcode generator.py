import qrcode
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text")
        qr = qrcode.make(text)
        qr.save("static/qrcode.png")
        return render_template("index.html", qr_image="static/qrcode.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
