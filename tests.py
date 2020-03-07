import unittest
from datetime import date, datetime
from flask_testing import TestCase
from app import app, db
from config import TestingConfig
from model import Task
import json

class TaskmanTestCase(TestCase):
    def setUp(self):
        db.create_all()
        # Add testing tasks to DB
        db.session.add(Task(subject = "Testing task 1", due_date = date.today()))
        db.session.add(Task(subject = "Testing task 2", due_date = date.today()))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_app(self):
        # Apply testing config
        app.config.from_object(TestingConfig)
        return app

    def test_list_tasks(self):
        result = self.client.get('/tasks/')
        self.assertEqual(result.status_code, 200)
        
    def test_get_task_by_id(self):
        result = self.client.get('/tasks/1')
        self.assertEqual(result.status_code, 200)

    def test_fail_get_task_by_nonexisting_id(self):
        result = self.client.get('/tasks/0')
        self.assertEqual(result.status_code, 404)

    def test_create_task(self):
        result = self.client.post('/tasks/',
            data=json.dumps({'subject': 'Testing task 3'}), 
            content_type='application/json')
        self.assertEqual(result.status_code, 201)

    def test_fail_create_task_bad_request(self):
        result = self.client.post('/tasks/',
            data=json.dumps({'subject1': 'Testing task 3'}), 
            content_type='application/json')
        self.assertEqual(result.status_code, 400)


    def test_delete_task_by_id(self):
        result = self.client.delete('/tasks/2')
        self.assertEqual(result.status_code, 200)
    
    def test_fail_delete_task_by_nonexisting_id(self):
        result = self.client.delete('/tasks/0')
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
