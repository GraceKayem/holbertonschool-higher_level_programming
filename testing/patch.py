#!/usr/bin/env python3
import requests

"""
Next up, you’ll use requests.patch() to modify the value of a specific field on an existing todo. 
PATCH differs from PUT in that it doesn’t completely replace the existing resource. 
It only modifies the values set in the JSON sent with the request.
"""

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
#call response.json(), you can see that title was updated to Mow lawn
print(response.json())

print(response.status_code)
