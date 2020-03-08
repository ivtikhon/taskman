import requests
import json
from tabulate import tabulate
import argparse
import pprint
from datetime import date, datetime


API_ENDPOINT = 'http://127.0.0.1:5000/tasks/'   # Assign endpoint here

def list_tasks(expring_today = False):
    res = requests.get(url = API_ENDPOINT)
    tasks = [['Id', 'Subject', 'Due date']]
    today = datetime.now().date()
    if(res.status_code == 200):
        for task in res.json()['tasks']:
            due_date = datetime.strptime(task['due_date'], "%m/%d/%Y").date()
            if expring_today and due_date > today:
                continue
            tasks.append([task['id'], task['subject'], task['due_date']])
    if len(tasks) > 1:
        print(tabulate(tasks, headers = 'firstrow'))

def add_task(subject, due_date = None):
    data = {'subject': subject}
    headers = {'content-type': 'application/json'}
    if due_date:
        try:
            # Check date format
            date_time_obj = datetime.strptime(args.due_date, "%m/%d/%Y")
        except:
            print("Due date format is MM/DD/YYY")
            exit(1)
        data['due_date'] = due_date
    res = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
    if res.status_code != 201:
        print('Failed to add task, see error log for details')
        exit(1)

def del_task(id):
    res = requests.delete(url = API_ENDPOINT + '/' + str(id))
    if res.status_code != 200:
        print('Failed to delete task, see error log for details')
        exit(1)

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(prog='taskman')
    subparsers = parser.add_subparsers(dest='command', help ='commands')
    list_parser = subparsers.add_parser('list', help = 'list tasks')
    list_parser.add_argument('--expiring-today', help = 'tasks that are due today', action='store_true')

    create_parser = subparsers.add_parser('add', help='add a task')
    create_parser.add_argument('subject', action='store', help='task subject')
    create_parser.add_argument('due_date', action='store', help='due date')

    delete_parser = subparsers.add_parser('done', help='close a task')
    delete_parser.add_argument('id', action='store', help='id of the task to close')

    args = parser.parse_args()

    # Process commands
    if args.command == 'add':
        date_time_obj = None
        add_task(subject = args.subject, due_date = args.due_date)
    elif args.command == 'list':
        list_tasks(args.expiring_today)
    elif args.command == 'done':
        del_task(args.id)
