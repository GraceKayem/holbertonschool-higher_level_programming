#!/usr/bin/env python3
import requests

"""
Beyond GET and POST, requests provides support for all the other HTTP methods you would use with a REST API. 
The following code sends a PUT request to update an existing todo with new data. 
Any data sent with a PUT request will completely replace the existing values of the todo.

You’ll use the same JSONPlaceholder endpoint you used with GET and POST, but this time you’ll append 10 to the end of the URL. 
This tells the REST API which todo you’d like to update:
"""

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
#call requests.get() to view the contents of the existing todo
print(response.json())

todo = {"userId": 1, "title": "Wash car", "completed": True}
#call requests.put() with new JSON data to replace the existing to-do’s values
response = requests.put(api_url, json=todo)
#see the new values when you call response.json()
print(response.json())

print(response.status_code)

#successful PUT requests will always return 200 instead of 201 because you aren’t creating a new resource but just updating an existing one.
