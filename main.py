from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    keywords = request.form['keywords']
    print("Text input: ${keywords}")
    return redirect(url_for('main'))

app.run()