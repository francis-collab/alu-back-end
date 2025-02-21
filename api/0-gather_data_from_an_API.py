#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress from an API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_res = requests.get("{}/users/{}".format(url, emp_id))
    user_data = user_res.json()
    emp_name = user_data.get("name")

    # Fetch tasks
    todos_res = requests.get("{}/todos?userId={}".format(url, emp_id))
    todos_data = todos_res.json()

    # Process tasks
    completed_tasks = [task.get("title") for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    num_completed = len(completed_tasks)

    # Display results
    print("Employee {} is done with tasks({}/{}):".format(emp_name, num_completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
