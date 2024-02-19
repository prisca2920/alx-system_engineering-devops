#!/usr/bin/python3
"""gathering data from an api"""
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

    with open('{}.csv'.format(employeeId), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, task.get('completed'),
                            task.get('title')))
