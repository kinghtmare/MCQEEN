def print_menu():
    print("\n🏁 LIGHTNING MCQUEEN'S TO-DO LIST 🏁")
    print("Gotta get ready for the big race! Here's what's on deck:")
    print("1. Add a task")
    print("2. View my to-do list")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")
 
 
def add_task(tasks):
    task_name = input("What's the task, Lightning? ").strip()
    if not task_name:
        print("Can't add an empty task.Try again.")
        return
    tasks.append({"name": task_name, "done": False})
    print(f'Added to your list: "{task_name}"')
 
 
def view_tasks(tasks):
    if not tasks:
        print("there is no tasks yet ")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "[DONE]" if task["done"] else "[PENDING]"
        print(f"{i}. {status} {task['name']}")
 
 
def get_task_index(tasks, prompt):

    if not tasks:
        print("Your list is empty — nothing to select.")
        return None
 
    view_tasks(tasks)
    raw = input(prompt).strip()
 
    if not raw.isdigit():
        print("That's not a valid task number.")
        return None
 
    index = int(raw) - 1
    if index < 0 or index >= len(tasks):
        print("No task with that number.")
        return None
 
    return index
 
 
def complete_task(tasks):
    index = get_task_index(tasks, "Which task number is done? ")
    if index is None:
        return
    if tasks[index]["done"]:
        print(f'"{tasks[index]["name"]}" is already marked as done.')
    else:
        tasks[index]["done"] = True
        print(f'Checked off: "{tasks[index]["name"]}"')
 
 
def remove_task(tasks):
    index = get_task_index(tasks, "Which task number do you want to remove? ")
    if index is None:
        return
    removed = tasks.pop(index)
    print(f'Removed from your list: "{removed["name"]}"')
 
 
def main():
    tasks = []
    print("Hey there, Lightning McQueen! Let's get you organized before race day.")
 
    while True:
        print_menu()
        choice = input("What's the move, Lightning? ").strip()
 
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Speed. I am speed. Catch you at the finish line, Lightning! 🏎️")
            break
        else:
            print("That's not on the menu. Pick 1-5.")
 
 
if __name__ == "__main__":
    main()
 