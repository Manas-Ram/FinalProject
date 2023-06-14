# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path="", static_folder="static")
@app.route('/index')
def index():


    f = open("templates/borough.json", "r")
    data = json.load(f)
    f.close()

    return render_template('index.html', data = data)
@app.route('/')
def about():

    return render_template('about.html')
@app.route('/micro')
def micro():


    f = open("templates/borough.json", "r")
    data = json.load(f)
    f.close()

    return render_template('micro.html', data = data)
@app.route('/bedstuy')
def bedstuy():
    return render_template('bedstuy.html')
@app.route('/jacksonheights')
def jacksonheights():
    return render_template('jacksonheights.html')
@app.route('/harlem')
def harlem():
    return render_template('harlem.html')
@app.route('/williamsburg')
def williamsburg():
    return render_template('williamsburg.html')
@app.route('/parkslope')
def parkslope():
    return render_template('parkslope.html')
@app.route('/bayside')
def bayside():
    return render_template('bayside.html')

app.run(debug=True)


