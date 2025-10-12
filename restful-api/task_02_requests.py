#!/usr/bin/env python3
"""
Create a function fetch_and_print_posts() that fetches all posts from JSONPlaceholder.
Create a function fetch_and_save_posts() that fetches all posts from JSONPlaceholder.
"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    # Set the API URL
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request
    response = requests.get(api_url)
    
    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse and print titles
    if response.status_code == 200:
        # Convert response to JSON (list of dicts)
        data = response.json()
        
        # Loop through the data and print titles
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to posts.csv."""
    # Set the API URL
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send GET request
    response = requests.get(api_url)

    # Check if successful
    if response.status_code == 200:
        # Convert response to JSON
        data = response.json()

        # Extract only id, title, and body
        posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        # Writing data into posts.csv
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            
            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header row
            writer.writerows(posts)  # Write all post rows

        # Print success message
        print("Posts saved successfully to posts.csv")
    else:
        # Print error message if request failed
        print(f"Request failed with status code: {response.status_code}")
