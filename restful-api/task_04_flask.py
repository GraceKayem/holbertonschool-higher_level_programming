#!/usr/bin/env python3
"""
Flask API to manage users with GET and POST endpoints.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary, stored in memory
# Key: username, Value: user dictionary
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    """Return a welcome message at root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return full user data or error if user not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON POST data."""
    data = request.get_json()

    # Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Add user to dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
