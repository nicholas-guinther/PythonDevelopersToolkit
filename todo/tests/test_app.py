import pytest
from todo.api import get_tasks, create_task, finish_task, delete_task


@pytest.mark.xfail(reason="This test fails because we don't have create_task function")
def test_list_tasks(test_app):
    # Make sure no tasks exist
    assert get_tasks() == []
    # Create some tasks
    create_task("buy milk")
    create_task("buy cookies")
    # Make sure we have 2 tasks now
    assert len(get_tasks()) == 2


# TODO: Write tests to create/delete/finish a task
def test_create_task(test_app):
    create_task('Get milk')
    existing_task = get_tasks()
    assert len(get_tasks()) == 1
    first_task = existing_task[0]
    assert first_task.body == 'Get milk'
    assert first_task.done is False


def test_finish_task(test_app):
    create_task('Get Milk')
    assert len(get_tasks()) == 1

    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    finish_task(get_milk_id)

    get_milk = get_tasks().pop()
    assert get_milk.done is True


def test_delete_task(test_app):
    create_task('Get Milk')
    assert len(get_tasks()) == 1

    get_milk = get_tasks().pop()
    get_milk_id = get_milk.id
    delete_task(get_milk_id)

    assert len(get_tasks()) == 0
