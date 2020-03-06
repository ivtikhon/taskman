import requests
import json
from tabulate import tabulate

API_ENDPOINT = 'http://127.0.0.1:5000/tasks/'

def printTask(task):
    print('id: ' + str(task['id']) + ' subject: ' + task['subject'] + ' due date: ' + task['due_date'])

def listTasks():
    res = requests.get(url = API_ENDPOINT)
    tasks = [['Id', 'Subject', 'Due date']]
    if(res.status_code == 200):
        for task in res.json()['tasks']:
            tasks.append([task['id'], task['subject'], task['due_date']])
    print(tabulate(tasks, headers = 'firstrow'))

def addTask(subject, due = None):
    data = {'subject': subject}
    headers = {'content-type': 'application/json'}
    if due:
        data['due_date'] = due
    res = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
    if res.status_code != 201:
        print('Failed to add task, see error log for details')
        exit(1)


if __name__ == '__main__':
    # addTask("Collect input from stakeholders for weekly status meeting", "4/8/2020")
    listTasks()