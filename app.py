from get_request_to_api import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/nearbyrestaurants')
def find_restaurants():
    find_restaurants = find_local_restaurants("EC4M7RF")
    find_restaurants.get_request()
    closest_restaurants = find_restaurants.closest_restaurants(10)
    return render_template("index.html", form=closest_restaurants)

if __name__ == "__main__":
    app.run()
