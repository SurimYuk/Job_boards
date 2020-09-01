from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Super Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        fromDB = db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", gotWord=word, resultsNumber=len(jobs))


app.run(host="0.0.0.0")
