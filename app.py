from flask import Flask, render_template, request
from weather import main as get_weather
import requests


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    current_weather = None
    forecast = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        current_weather, forecast = get_weather(city, state, country)
    return render_template('index.html', current_weather=current_weather, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
