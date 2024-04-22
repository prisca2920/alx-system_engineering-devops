#!/usr/bin/python3
"""export data in the JSON format"""

import json
from requests import get
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}

    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as f:
        json.dump(dictionary, f)
