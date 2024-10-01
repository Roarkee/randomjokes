from flask import Flask, render_template, url_for, request
import requests

app=Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    url="https://v2.jokeapi.dev/joke/Any"
    response=requests.get(url).json()

    return render_template("index.html", response=response)

if __name__=="__main__":
    app.run(debug=True)
