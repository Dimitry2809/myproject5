from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import flash

app= Flask(__name__)
app.config['SECRET_KEY'] = "awsdefretrthyetjetyjsfgbxcvbsfgthjsfdgsfdga"



menuUp = [
    {"name":"Головна", "url":"hauptseit"},
    {"name":"Запитання", "url":"fragen"},
    {"name":"Реeстрацiя", "url":"registrirung"}
]

@app.route("/")
def index():
    return render_template("index.html", titel = "головна", menu = menuUp)

@app.route("/registrirung", methods=["POST", "GET"])
def registrirung():
    if request.method == "POST":
        print(len(request.form["username"]))
        if len(request.form['username']) > 2:
            flash("Повiдомлення вiдправлено!", category="success")
        else:
            flash("Помилка: занадто мало букв!", category="error")

    return render_template("registrirung.html")

if __name__ == "__main__":
    app.run(debug=True)