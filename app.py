import requests

postcode = "EC4M7RF"
url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
headers = {
    "Host": "uk.api.just-eat.io",
    "User-Agent": "Foo bar"
}

response = requests.get(url, headers=headers)
print(response)

for restaurant in (response.json()["restaurants"])[0:10]:
    print (restaurant["name"])
    print (restaurant["address"]["firstLine"])
    print(restaurant["address"]["postalCode"])
    print(restaurant["rating"]["starRating"])
    print(restaurant["cuisines"][0]["name"])
