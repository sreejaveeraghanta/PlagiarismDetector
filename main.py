from flask import Flask, request, redirect, url_for, render_template
import functions

app = Flask(__name__)

# Home page route
@app.route("/") 
def home():
    return render_template("index.html")

# File input page 
@app.route("/fileInput")
def fileInput():
    return render_template("fileInput.html")

# Validating the file input from the file input page
@app.route("/fileInput", methods=['POST'])
def fileInputRead(): 
    file = request.form['file']
    if (file != ""):
        return "The similarity is: "
    else: 
        return render_template("fileInput.html", errorFileInput="Invalid: please choose a file")

# Double file input page
@app.route("/fileVsfile")
def fileVsfile():
    return render_template("fileVsfile.html")

# Validating both files from the double file input page
@app.route("/fileVsfile", methods=['POST'])
def filesInputRead(): 
    file1 = request.form['file1']
    file2 = request.form['file2']
    if (file1 != "" or file2 != ""):
        return "The similarity is: " + functions.checkSimilarity(file1, file2)
    else: 
        return render_template("fileVsfile.html", errorFilesInput="Invalid: please choose two files")

# Text input page
@app.route("/textInput")
def textInput():
    return render_template("textInput.html")

# Validating the text input
@app.route("/textInput", methods=['POST'])
def textInputRead(): 
    text = request.form['text']
    if (text != ""):
        return "The similarity is: "
    else: 
        return render_template("textInput.html", errorTextInput="Invalid: please type something")

# Double text input page
@app.route("/textVstext")
def textVStext():
    return render_template("textVstext.html")

# Validating both text inputs
@app.route("/textVstext", methods=['POST'])
def textsInputRead(): 
    text1 = request.form['text1']
    text2 = request.form['text2']
    if (text1 != "" and text2 != ""):
        return "The similarity is: " + functions.checkSimilarity(text1, text2)
    else: 
        return render_template("textVstext.html", errorTextsInput="Invalid: please type something in both text fields")

# Running the app
if __name__ == "__main__":
    app.run()

