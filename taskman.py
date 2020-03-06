import requests
import json
from tabulate import tabulate
import argparse
import pprint

API_ENDPOINT = 'http://127.0.0.1:5000/tasks/'   # Assign endpoint here

def listTasks():
    res = requests.get(url = API_ENDPOINT)
    tasks = [['Id', 'Subject', 'Due date']]
    if(res.status_code == 200):
        for task in res.json()['tasks']:
            tasks.append([task['id'], task['subject'], task['due_date']])
    print(tabulate(tasks, headers = 'firstrow'))

def addTask(subject, due_date = None):
    data = {'subject': subject}
    headers = {'content-type': 'application/json'}
    if due_date:
        data['due_date'] = due_date
    res = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
    if res.status_code != 201:
        print('Failed to add task, see error log for details')
        exit(1)

def delTask(id):
    res = requests.delete(url = API_ENDPOINT + '/' + str(id))
    if res.status_code != 200:
        print('Failed to delete task, see error log for details')
        exit(1)

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(prog='taskman.py')
    subparsers = parser.add_subparsers(dest='command', help='commands')
    list_parser = subparsers.add_parser('list', help='List tasks')

    create_parser = subparsers.add_parser('add', help='Add a task')
    create_parser.add_argument('subject', action='store', help='Task subject')
    create_parser.add_argument('due_date', action='store', help='Due date')

    delete_parser = subparsers.add_parser('done', help='Close a task')
    delete_parser.add_argument('id', action='store', help='Id of the task to close')

    args = parser.parse_args()

    if args.command == 'add':
        addTask(subject = args.subject, due_date = args.due_date)
    elif args.command == 'list':
        listTasks()
    elif args.command == 'done':
        delTask(args.id)
