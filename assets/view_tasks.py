
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}.{task}")

            

