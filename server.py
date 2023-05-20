# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path="", static_folder="static")
@app.route("/")
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    lecan = []
    for x in data["Canada"].values():
        lecan.append(x)
    leus = []
    for x in data["United States"].values():
        leus.append(x)
    lemex = []
    for x in data["Mexico"].values():
        lemex.append(x)
    CanadaLine = []
    for i in range(len(lecan) - 1):
        CanadaLine.append([lecan[i], lecan[i + 1]])
    UsLine = []
    for i in range(len(leus) - 1):
        UsLine.append([leus[i], leus[i + 1]])
    MexLine = []
    for i in range(len(lemex) - 1):
        MexLine.append([lemex[i], lemex[i + 1]])
    ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    years = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
    return render_template("index.html", years=data["Canada"].keys(),Canada=CanadaLine,Us=UsLine,Mex=MexLine,ages=ages,years2=years,
    )

@app.route("/year")
def year():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    year = request.args.get("year")
    Mex = 90 - ((data["Mexico"][year]) - 50) * 2
    Canada = 90 - ((data["Canada"][year]) - 50) * 2
    Us = 90 - ((data["United States"][year]) - 50) * 2
    years = [["Mexico", data["Mexico"][year]],["Canada", data["Canada"][year]],["United States", data["United States"][year]],
    ]
    return render_template(
        "year.html", year=year, Mex=Mex, Us=Us, Canada=Canada, years=years
    )


app.run(debug=True)
