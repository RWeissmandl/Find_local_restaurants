import requests

postcode = "M74FR"
url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/cb2"

headers = {
    "Host": "uk.api.just-eat.io",
    "User-Agent": "Foo bar"
}

response = requests.get(url, headers=headers)

print (response.json())
