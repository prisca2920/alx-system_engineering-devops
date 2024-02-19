#!/usr/bin/python3
"""gathering data from an api"""
from requests import get
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId
    reply = get(url)
    userName = reply.json().get('name')

    todoUrl = url + "/todos"
    reply = get(todoUrl)
    tasks = reply.json()
    complete = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            complete += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(userName, complete, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
