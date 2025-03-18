from flask import Flask
from flask import render_template
from flask import url_for

app= Flask(__name__)

menuUp = [
    {"name":"Головна", "url":"hauptseit"},
    {"name":"Запитання", "url":"fragen"},
    {"name":"Реeстрацiя", "url":"registrirung"}
]

@app.route("/")
def index():
    return render_template("index.html", titel = "головна", menu = menuUp)

if __name__ == "__main__":
    app.run(debug=True)