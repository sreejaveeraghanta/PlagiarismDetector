from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/fileInput")
def fileInput():
    return render_template("fileInput.html")

@app.route("/fileVsfile")
def fileVsfile():
    return render_template("fileVsfile.html")

@app.route("/textInput")
def textInput():
    return render_template("textInput.html")

@app.route("/textVstext")
def textVStext():
    return render_template("textVstext.html")

if __name__ == "__main__":
    app.run()

