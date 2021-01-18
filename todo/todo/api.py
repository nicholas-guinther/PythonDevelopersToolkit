"""API functions to interact with TODO tasks."""

from todo.models import Task, db


def get_tasks():
    return Task.query.all()


def create_task(body):
    # TODO: add task to the database
    task = Task(body=body)
    db.session.add(task)
    db.session.commit()


def delete_task(task_id):
    # TODO: delete a task from the database
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()


def finish_task(task_id):
    # TODO: mark task as done
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()
