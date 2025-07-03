import json
import os

FILENAME = "tasks.json"

def load_tasks():
     if os.path.exists(FILENAME):
          with open(FILENAME, "r") as file:
               return json.load(file)
     return[]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
         json.dump(tasks, file, indent=4)



tasks = load_tasks()

def show_task(tasks):
            if not tasks:
                print("No Tasks available.")
                return
            for index, task in enumerate(tasks):
                status = "✅" if task["completed"] else "❌"
                print(f"{index + 1}, {task['title']} {status}") 


while True:
    print("\n ←——Task Manager——→")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice from 1 to 5: ")
    if choice=="1":
        task1 = input("Enter your first task: ")
        tasks.append({"title":task1,"completed":True})

        task2 = input("Enter your second task: ")
        tasks.append({"title":task2,"completed":False})

        show_task(tasks)
        
    
    elif choice=="2":
        if not tasks:
             print("There are no Tasks to View. Add your tasks to view.")
        else:
             show_task(tasks)
             
            
    elif choice=="3":
        task_number = int(input("Enter the task number to mark as completed: ")) -1
        tasks[task_number]["completed"] = True

        show_task(tasks)

    elif choice=="4":
        task_number = int(input("Enter the Task number to remove from your list: ")) -1
        tasks.pop(task_number)
        print("After deleting, the available tasks are:")
        show_task(tasks)



    elif choice=="5":
         save_tasks(tasks)
         print("Tasks saved. Exiting Task Manager.")
         break







    









