from flask import Flask
from flask import render_template

app= Flask(__name__)

menuUp = ["Головна", "Питання", "Регiстрацiя"]

@app.route("/")
def index():
    return render_template("index.html", titel = "головна", menu = menuUp)

if __name__ == "__main__":
    app.run(debug=True)