#!/usr/bin/python3
"""
A module that export python script into csv data
"""
import csv
import requests
import sys


if len(sys.argv) > 1:
    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get('name'), task
                             .get('completed'), task.get('title')])
