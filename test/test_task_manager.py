import json
from storage import TaskManager

def test_add_task(tmp_path):
    storage_file = tmp_path / "tasks.json"
    manager = TaskManager(storage_file)
    manager.add_task("Test Task", "Test Description", "Test Category", "2024-11-30", "Высокий")

    with open(storage_file, 'r') as file:
        tasks = json.load(file)
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Test Task"

def test_mark_task_completed(tmp_path):
    storage_file = tmp_path / "tasks.json"
    manager = TaskManager(storage_file)
    manager.add_task("Test Task", "Test Description", "Test Category", "2024-11-30", "Высокий")
    manager.mark_task_completed(1)

    with open(storage_file, 'r') as file:
        tasks = json.load(file)
        assert tasks[0]['status'] == "Выполнена"

def test_delete_task(tmp_path):
    storage_file = tmp_path / "tasks.json"
    manager = TaskManager(storage_file)
    manager.add_task("Test Task", "Test Description", "Test Category", "2024-11-30", "Высокий")
    manager.delete_task(1)

    with open(storage_file, 'r') as file:
        tasks = json.load(file)
        assert len(tasks) == 0

def test_search_tasks(tmp_path):
    storage_file = tmp_path / "tasks.json"
    manager = TaskManager(storage_file)
    manager.add_task("Test Task", "Test Description", "Test Category", "2024-11-30", "Высокий")
    tasks = manager.search_tasks(keyword="Test")
    assert len(tasks) == 1