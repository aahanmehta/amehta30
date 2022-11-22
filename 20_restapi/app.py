# Duo Double A 2.0: Aahan and April 
# SoftDev pd08
# K20: Restful API 
# 2022-11-21
# time spent: 0.5

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import requests                     #facilitate http requests

app = Flask(__name__)    #create Flask object

key_file = open("key_nasa.txt", "r") 
key = key_file.read()

get_the_thing = "https://api.nasa.gov/planetary/apod?api_key=" + key
the_thing = requests.get(get_the_thing)
thing_formatted = the_thing.json()
# print(thing_formatted)

@app.route('/')
def open_api():
    return render_template("main.html", title = thing_formatted['title'], explanation = thing_formatted['explanation'], url = thing_formatted['url'])


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
