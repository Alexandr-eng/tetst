from storage import TaskManager

def main():
    manager = TaskManager('data/tasks.json')

    while True:
        print("\nМенеджер задач")
        print("1. Просмотреть все задачи")
        print("2. Просмотреть задачи по категории")
        print("3. Добавить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Удалить задачу")
        print("6. Поиск задач")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            tasks = manager.get_tasks()
            for task in tasks:
                print(task.to_dict())
        elif choice == '2':
            category = input("Введите категорию: ")
            tasks = manager.get_tasks(category)
            for task in tasks:
                print(task.to_dict())
        elif choice == '3':
            title = input("Название: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = input("Срок выполнения (ГГГГ-ММ-ДД): ")
            priority = input("Приоритет (Низкий, Средний, Высокий): ")
            manager.add_task(title, description, category, due_date, priority)
            print("Задача добавлена!")
        elif choice == '4':
            task_id = int(input("Введите ID задачи: "))
            task = manager.mark_task_completed(task_id)
            if task:
                print(f"Задача {task.title} отмечена как выполненная.")
            else:
                print("Задача не найдена.")
        elif choice == '5':
            task_id = int(input("Введите ID задачи: "))
            manager.delete_task(task_id)
            print("Задача удалена.")
        elif choice == '6':
            keyword = input("Ключевое слово: ")
            category = input("Категория: ")
            status = input("Статус (Выполнена/Не выполнена): ")
            tasks = manager.search_tasks(keyword, category, status)
            for task in tasks:
                print(task.to_dict())
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()