#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching employee data")
        sys.exit(1)

    employee = response.json()
    employee_name = employee.get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching TODO list")
        sys.exit(1)

    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    done_tasks_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks_count, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
