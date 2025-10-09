#!/usr/bin/env python3
import requests

"""
to completely remove a resource, then you use DELETE. 

The requests library is an awesome tool for working with REST APIs and an indispensable part of your Python tool belt.
"""

api_url = "https://jsonplaceholder.typicode.com/todos/10"
#call requests.delete() with an API URL that contains the ID for the todo you would like to remove. 
#This sends a DELETE request to the REST API, which then removes the matching resource. 
response = requests.delete(api_url)
#After deleting the resource, the API sends back an empty JSON object indicating that the resource has been deleted
print(response.json())

print(response.status_code)