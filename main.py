from flask import Flask, request, redirect, url_for, render_template
from difflib import SequenceMatcher

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/fileInput")
def fileInput():
    return render_template("fileInput.html")
@app.route("/fileInput", methods=['POST'])
def fileInputRead(): 
    file = request.form['file']
    if (file != ""):
        return "The similarity is: "
    else: 
        return render_template("fileInput.html", errorFileInput="Invalid: please choose a file")

@app.route("/fileVsfile")
def fileVsfile():
    return render_template("fileVsfile.html")

@app.route("/fileVsfile", methods=['POST'])
def filesInputRead(): 
    file1 = request.form['file1']
    file2 = request.form['file2']
    if (file1 != "" or file2 != ""):
        return "The similarity is: "
    else: 
        return render_template("fileVsfile.html", errorFilesInput="Invalid: please choose two files")

@app.route("/textInput")
def textInput():
    return render_template("textInput.html")

@app.route("/textInput", methods=['POST'])
def textInputRead(): 
    text = request.form['text']
    if (text != ""):
        return "The similarity is: "
    else: 
        return render_template("textInput.html", errorTextInput="Invalid: please type something")

@app.route("/textVstext")
def textVStext():
    return render_template("textVstext.html")

@app.route("/textVstext", methods=['POST'])
def textsInputRead(): 
    text1 = request.form['text1']
    text2 = request.form['text2']
    if (text1 != "" or text2 != ""):
        return "The similarity is: "
    else: 
        return render_template("textVstext.html", errorTextsInput="Invalid: please type something in both text fields")

if __name__ == "__main__":
    app.run()

