from FishingApp import app

@app.route("/")
def index():
    return "Hello from flask home"
