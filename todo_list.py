def add_task(task, dict_tasks):
    new_dict = dict_tasks
    new_dict[task] = "not completed"
    return new_dict

def mark_task(task, dict_tasks):
    in_list = False
    
    for key in dict_tasks:
        if key == task:
            in_list = True
            dict_tasks[key] = "completed"
            
    return in_list

def mark_all(dict_tasks):    
    for key in dict_tasks:
        dict_tasks[key] = "completed"
            
    return dict_tasks

def delete_task(task, dict_tasks):
    in_list = False
    
    list_keys = []
    
    for key in dict_tasks:
        if key == task:
            in_list = True
            list_keys.append(key)
    
    for l in list_keys:
        del dict_tasks[l]
            
    return in_list
            

def main():
    dict_tasks = dict()
    action = ""
    
    while action.upper() != "DONE":
        action = input("\n\nEnter add, view, markall, delete, or done.")
        if action.upper() == "ADD":
            task = input("Enter the task you want to add.")
            add_task(task, dict_tasks)
            print("\nThe list is now:")
            print(dict_tasks)
        elif action.upper() == "VIEW":
            print(dict_tasks)
        elif action.upper() == "MARK":
            task = input("Enter the task you want to mark.")
            marked = mark_task(task, dict_tasks)
            if marked == False:
                print("\nThe task could not be marked.")
            print("\nThe list is now:")
            print(dict_tasks)
        elif action.upper() == "DELETE":
            task = input("Enter the task you want to delete.")
            deleted = delete_task(task, dict_tasks)
            if deleted == False:
                print("\nThe task could not be deleted.")
            print("\nThe list is now:")
            print(dict_tasks)
        elif action.upper() == "MARKALL":
            mark_all(dict_tasks)
            print("\nThe list is now:")
            print(dict_tasks)
            
main()