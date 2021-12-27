from flask import Flask, render_template

app = Flask(__name__, template_folder="")


@app.route("/")
def my_home_function():
    return render_template("my_html_template.html")
