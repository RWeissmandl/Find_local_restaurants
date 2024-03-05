from get_request_to_api import *
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route ('/', methods=['GET', 'POST'])
def find_restaurants():
    postcode = request.form.get('postcode', 'EC4M7RF')
    find_restaurants = find_local_restaurants(postcode)
    find_restaurants.get_request()
    closest_restaurants = find_restaurants.closest_restaurants(10)
    return render_template("index.html", form=closest_restaurants, postcode=postcode)

if __name__ == "__main__":
    app.run()
