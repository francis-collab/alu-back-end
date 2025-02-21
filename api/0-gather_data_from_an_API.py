#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API
This module uses a REST API to gather information about an employee's TODO list progress.
"""

import requests
import sys

def get_employee_data(employee_id):
    """
    Fetches the employee data from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing the employee's data.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def get_todo_list(employee_id):
    """
    Fetches the TODO list for the employee from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of dictionaries containing the TODO items.
    """
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee = get_employee_data(employee_id)
    if not employee:
        print("Error fetching employee data")
        sys.exit(1)

    employee_name = employee.get("name")
    todos = get_todo_list(employee_id)
    if not todos:
        print("Error fetching TODO list")
        sys.exit(1)

    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    done_tasks_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
