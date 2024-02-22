def add_task(task, dict_tasks):
    new_dict = dict_tasks
    new_dict[task] = "not completed"
    return new_dict

def main():
    dict_tasks = dict()
    action = ""
    
    while action.upper() != "DONE":
        action = input("\n\nEnter add, view, mark, delete, or done.")
        if action.upper() == "ADD":
            task = input("Enter the task you want to add.")
            add_task(task, dict_tasks)
            print("\nThe list is now:")
            print(dict_tasks)
        elif action.upper() == "view":
            print(dict_tasks)
        elif action.upper() == "mark":
            task = input("Enter the task you want to mark.")
            marked = mark_task(task, dict_tasks)
            if marked == False:
                print("\nThe task could not be marked.")
            print("\nThe list is now:")
            print(dict_tasks)
        elif action.upper() == "delete":
            task = input("Enter the task you want to delete.")
            deleted = delete_task(task, dict_tasks)
            if deleted == False:
                print("\nThe task could not be deleted.")
            print("\nThe list is now:")
            print(dict_tasks)
            
main()