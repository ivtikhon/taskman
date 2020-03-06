from datetime import date, datetime
from app import app, db
from model import Task
from flask import jsonify, request, Response
import json

# Create a task
@app.route('/tasks/', methods=['POST'])
def create_task():
    taskRequest = request.get_json()
    status = 201 # Success
    message = ""
    if 'subject' in taskRequest:
        dueDate = date.today()
        if 'due_date' in taskRequest:
            dueDate = datetime.strptime(taskRequest['due_date'], '%m/%d/%Y').date()
        newTask = Task(subject = taskRequest['subject'], due_date = dueDate)
        db.session.add(newTask)
        db.session.commit()
        if not app.testing:
            app.logger.info("Created task with subject \"%s\"", taskRequest['subject'])
    else:
        message = json.dumps({"error": "Invalid request format"})
        status = 400 # Bad request
        if not app.testing:
            app.logger.error("Failed to create task: invalid request format")
    return Response(message, status = status, mimetype = 'application/json')

# List all tasks
@app.route('/tasks/', methods=['GET'])
def list_tasks():
    tasks = [{'id': task.id, 'subject': task.subject, 'due_date': task.due_date.strftime("%m/%d/%Y")} for task in Task.query.all()]
    return jsonify({'tasks': tasks})

# Get a task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = Task.query.get(id)
    response = None
    if task:
        response = jsonify({'id': task.id, 'subject': task.subject, 'due_date': task.due_date.strftime("%m/%d/%Y")})
    else:
        response = Response("", status = 404, mimetype = 'application/json') 
    return response

# Delete a task by id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_by_id(id):
    task = Task.query.get(id)
    status = 200 # Success
    if task:
        subject = task.subject
        db.session.delete(task)
        db.session.commit()
        if not app.testing:
            app.logger.info("Deleted task with subject \"%s\"", subject)
    else:
        status = 404  # Not found
        if not app.testing:
            app.logger.error("Failed to delete task: object not found")
    return Response("", status = status, mimetype = 'application/json')