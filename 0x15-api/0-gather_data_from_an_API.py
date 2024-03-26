#!/usr/bin/python3
import requests
import sys
"""
Gather data from an API
"""


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        response = requests.get(todos_url)
        response.raise_for_status()
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)

    try:
        response = requests.get(f"{base_url}/users/{employee_id}")
        response.raise_for_status()
        employee_name = response.json()["name"]
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks ({}"
          "/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for todo in completed_tasks:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))
