from assets.view_tasks import view_tasks

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f" Task '{removed}' deleted successfully!")
            else:
                print(" Invalid task number.")
        except ValueError:
            print(" Please enter a valid number.")
