#!/usr/bin/env python3
# app.py

"""
In this section, you’ll look at three popular frameworks for building REST APIs in Python. Each framework has pros and cons, so you’ll have to evaluate which works best for your needs. To this end, in the next sections, you’ll look at a REST API in each framework. All the examples will be for a similar API that manages a collection of countries.

Each country will have the following fields:

name is the name of the country.
capital is the capital of the country.
area is the area of the country in square kilometers.
The fields name, capital, and area store data about a specific country somewhere in the world.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial in-memory data
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    """Return the next available ID based on existing countries.
      This helper function uses a generator expression to select all the country IDs and then calls max() on them to get the largest value. 
      It increments this value by 1 to get the next ID to use.
    """
    return max(country["id"] for country in countries) + 1

#This code uses @app.get(), a Flask route decorator, to connect GET requests to a function in the application. 
# When you access /countries, Flask calls the decorated function to handle the HTTP request and return a response.
#In the code above, get_countries() takes countries, which is a Python list, and converts it to JSON with jsonify(). 
# This JSON is returned in the response.

@app.get("/countries")
def get_countries():
    """Return the full list of countries."""
    return jsonify(countries)
#In get_countries(), you need to use jsonify() because you’re returning a list of dictionaries and not just a single dictionary. 
# Flask doesn’t automatically convert lists to JSON.


#This function performs the following operations:
#Using request.is_json to check that the request is JSON
#Creating a new country instance with request.get_json()
#Finding the next id and setting it on the country
#Appending the new country to countries
#Returning the country in the response along with a 201 Created status code
#Returning an error message and 415 Unsupported Media Type status code if the request wasn’t JSON
#add_country() also calls _find_next_id() to determine the id for the new country:

@app.post("/countries")
def add_country():
    """Add a new country from JSON data."""
    if request.is_json:
        #uses the Flask request object to get information about the current HTTP request:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return jsonify(country), 201
    return jsonify({"error": "Request must be JSON"}), 415

if __name__ == "__main__":
    app.run(debug=True)

