# Find local restaurants

This app allows you to search for local restaurants based on a given postcode. It returns 10 local restaurants with restaurant name, address, rating and cuisine.

# How to run the app

This is a Python app using Flask web server. Download the folder, once folder has been downloaded locally, navigate into the folder via the terminal. Install dependencies required by running `pip install -r requirements.txt`. Run with the command `python app.py`. Ensure Flask is running. Open a browser and navigate to localhost. Flask runs on port:5000 by default. There is no specified route for simpility. 

# Improvements 

- This app has no error handling. I would use "try/except" to do basic error handling. 
- This app has no tests. I would use pytest to create tests, for example, one test would be to assert status.code == 200.
- An added feature could be to allow users to specify how many restarants to return. This app is hardcoded to return 10.  

# Unclear

The json response included multiple items for some of the requested data points. For example, address included city and lon/lat. Cuisines returned values for a variety of factors. Instructions specified clearly that a 'huge list of data' should not be returned. Therefore, I picked out the essential elements only.