import requests

class find_local_restaurants():
    def __init__(self, postcode):
        self.postcode = postcode
        self.url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
        self.headers = {
            "Host": "uk.api.just-eat.io",
            "User-Agent": "Foo bar"
        }
    def get_request(self):
        self.response = requests.get(self.url, headers=self.headers)

    def closest_restaurants(self, number_of_restaurants):
        restaurants = []
        for restaurant in (self.response.json()["restaurants"])[0:number_of_restaurants]:
            restaurants.append({
                "name": restaurant["name"],
                "address": restaurant["address"]["firstLine"],
                "postcode": restaurant["address"]["postalCode"],
                "rating": restaurant["rating"]["starRating"],
                "cuisine_name": restaurant["cuisines"][0]["name"]
            })
        return restaurants
