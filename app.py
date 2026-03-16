import requests
from flask import Flask, render_template
from flask import request
from weather import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        location = request.form["spot"]
        weather = get_weather(location)
        return(render_template("index.html", weather=weather))
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)