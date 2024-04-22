#!/usr/bin/python3
"""returns information about employees TODO list progress."""

from requests import get
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = get(todoUrl)
    tasks = response.json()
    result = 0
    completed = []

    for task in tasks:
        if task.get('completed'):
            completed.append(task)
            result += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, result, len(tasks)))

    for task in completed:
        print("\t {}".format(task.get('title')))
