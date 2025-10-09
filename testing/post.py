#!/usr/bin/env python3
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}

headers = {"Content-Type":"application/json"}
#call requests.post() to create a new todo in the system
#call json.dumps(todo) to serialize it
#The data argument tells requests what data to include in the request
#pass the headers dictionary to requests.post() to set the HTTP headers manually
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
#call response.json() to view the JSON
#The JSON includes a generated id for the new todo. The 201 status code tells you that a new resource was created
print(response.json())

print(response.status_code)
