#!/usr/bin/python3
"""exporting to json"""
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId
    reply = get(url)
    username = reply.json().get('name')

    todoUrl = url + "/todos"
    reply = get(todoUrl)
    tasks = reply.json()

    dict = {employeeId: []}
    for task in tasks:
        dict[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as f:
        json.dump(dict, f)
