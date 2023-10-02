from flask import render_template, jsonify, request, redirect, flash
import requests, json
from weatherapp import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/search_weather")
def weather():

    city = request.args.get("city")
    units = "metric"

    # Connect to OpenWeatherMap API
    app_secret_key = '78347ytqoahg7h34tq23'

    api_key = "0d7489523d4eae83df3879a8958fabbe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}&key={app_secret_key}"


    # Send the GET request to the API
    response = requests.get(url)

    # if successful
    if response.status_code == 200: 

        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        return render_template("index.html", city = city, data = data)
    else:
        flash("Unable to retrieve Weather Data...")
        return redirect("/home")



@app.route("/auto_vpn_locator")
def auto_vpn_locator():

    city = get_city_by_ip()
    units = "metric"

    # Connect to OpenWeatherMap API
    app_secret_key = '78347ytqoahg7h34tq23'

    api_key = "0d7489523d4eae83df3879a8958fabbe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}&key={app_secret_key}"


    # Send the GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
       
        return render_template("index.html", city=city, data=data)
    else:
        flash("Unable to retrieve Weather Data...")
        return redirect("/home")



#GET CITY BY IP
def get_city_by_ip():
    # url = "https://ipinfo.io/json"
    url = "https://ip-api.com/json"
    # url = "https://ip-api.io/json"

    response = requests.get(url)

    data = response.json()
    city = data

    return city
