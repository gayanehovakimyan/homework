todo_list = []

def add_tasks():
    while True:
	
        task_description = input("Enter tasks to your todo list: ")
        stop=int(input('If you want to stop press, 1: else press 2:'))
        if stop==1:
            break
        elif stop==2:
            if task_description:
                unique_id = len(todo_list) + 1
                priority = "medium"
                complete = False
                task = {'id': unique_id,
                    'description': task_description,
                    'priority': priority,
                    'completed': False}
                todo_list.append(task)
                print(f"Your task id.{unique_id}: {task_description} added to your todo list:")
            else:
                return "You should write task on your todo list"
        

        
add_tasks()


def removal():
    try:
        remover = int(input("Enter the ID you want to remove: "))
        for task in todo_list:
            if task['id'] == remover:
                todo_list.remove(task)
                print(f"ID {remover} found and removed from todo list.")

    except ValueError:
        print( "Please enter the correct ID (integer)")
removal()

def listing():
    check=input('Do you want to check your todo list? (y/n).:').lower()
    if check=='n':
        if not todo_list:
            print("There are no tasks in the to-do list.")
    elif check=='y':
        for task in todo_list:
            print(f"ID: {task['id']}, Description: {task['description']}")
listing()




def completion():
    task_id = int(input("Enter the ID you want to complete: "))
    
    for task in todo_list:
        if task['id'] == task_id:
            print(f"Task ID: {task_id}, Description: {task['description']}, Priority: {task['priority']}")
            user_choice = input("Do you want to complete this task? (y/n): ").lower()

            if user_choice == 'y':
                task['completed'] = True
                print(f'Task ID {task_id} is successfully marked as completed.')
            elif user_choice == 'n':
                print(f'Task ID {task_id} remains not completed.')
            else:
                print("Invalid choice. Task completion status remains unchanged.")

            return

    print("Task not found")
completion()

def prioritization():
    task_id = int(input("Enter the ID you want to prioritize: "))
    priory = int(input("Enter the priority type (1-low, 2-medium, 3-high): "))
    for task in todo_list:
        if task_id == task['id']:
            if priory == 1:
                task['priority'] = "low"
                print(f"Priority of {task_id} is set to low.")
            elif priory == 2:
                task['priority'] = "medium"
                print(f"Priority of {task_id} is set to medium.")
            elif priory == 3:
                task['priority'] = "high"
                print(f"Priority of {task_id} is set to high.")
            else:
                print( "Invalid priority type.")

    	print ("Task not found.")
prioritization()

