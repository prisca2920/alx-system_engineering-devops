#!/usr/bin/python3
"""export data in the CSV format"""

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

    with open('{}.csv'.format(employeeId), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, task.get('completed'),
                            task.get('title')))
