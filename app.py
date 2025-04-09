from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")  # ← 이 부분 추가!
def products():
    return render_template("products.html")

@app.route("/english")
def english():
    return render_template("english.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
