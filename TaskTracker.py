# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import argparse
from html import parser
import json
import os
import datetime

#move this somewhere else later
tasks = {
        "id": 0,
        "description": "",
        "status": "",
        "createdAt": "",
        "updatedAt": ""
    }

def task_add(task_name):
#check if task name already exists and if json file exists
#add the new dictionary inside the list of the dictionary within the json file
    if os.path.isfile("./tasks.json") == True :
        with open('tasks.json', 'r') as f:
            json_file = json.load(f)
            
            if any(task['description'] == task_name for task in json_file["tasks"]):
                print("Task already exists.")
            
            else:
                json_file["tasks"].append(
                    {
                    'id': json_file["tasks"][-1].get('id')+1,
                    'description': task_name,
                    "status": "todo",
                    'createdAt': datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                    "updatedAt": ""
                    }
            )
        
        with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)

        print("Task added successfully. ID:", json_file["tasks"][-1].get('id'))

    else:
        json_data = {
            "tasks": [
                {
                    "id": 1,
                    "description": task_name, 
                    "status": "todo",
                    "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                    "updatedAt": ""
                    }
                ]
        }
        with open('tasks.json', 'w') as f:
            json.dump(json_data, f, indent=4)
        print("Task added successfully. ID:", json_file["tasks"][-1].get('id'))


    
def task_update(task_id, new_description):
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)
            
            for task in json_file["tasks"]:
                if task['id'] == task_id:
                    task['description'] = new_description
                    task['updatedAt'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
                    print("Task updated successfully.")

    with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)
                    

def task_delete(task_id):
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)
            
            for task in json_file["tasks"]:
                if task['id'] == task_id:
                    json_file["tasks"].remove(task)
                    print("Task deleted successfully.")

    with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)

def task_in_progress(task_id, ):
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)
            
            for task in json_file["tasks"]:
                if task['id'] == task_id:
                    task['status'] = "in progress"
                    task['updatedAt'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
                    print("Task updated successfully.")

    with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)

def task_done(task_id):
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)
            
            for task in json_file["tasks"]:
                if task['id'] == task_id:
                    task['status'] = "done"
                    task['updatedAt'] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
                    print("Task updated successfully.")

    with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)

def task_list_all():
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)

            for task in json_file["tasks"]:
                    #make output more readable later
                    print(task)

def task_list_todo():
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)

            for task in json_file["tasks"]:
                if task['status'] == "todo":
                    print(task)

def task_list_done():
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)

            for task in json_file["tasks"]:
                if task['status'] == "done":
                    print(task)          

def task_list_in_progress():
    with open('tasks.json', 'r') as f:
            json_file = json.load(f)

            for task in json_file["tasks"]:
                if task['status'] == "in progress":
                    print(task)          


def main():
#wont run if json has errors
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    parser.add_argument('-add', type = str, metavar = '[Task Name]', default = None, help = 'Add a new task')
    parser.add_argument('-update', nargs=2,  metavar = ('[Task ID]', '[New Task Description]'), default = None, help = 'Update a task')
    parser.add_argument('-delete', type = int, metavar = '[Task ID]', default = None, help = 'Delete a task')
    parser.add_argument('-in-progress', type = int, metavar = '[Task ID]', default = None, help = 'Mark a task as in progress')
    parser.add_argument('-done', type = int, metavar = '[Task ID]', default = None, help = 'Mark a task as done')
    parser.add_argument('-list-all', action='store_true', help = 'List all tasks')
    parser.add_argument('-list-done', action='store_true', help = 'List done tasks')
    parser.add_argument('-list-todo', action='store_true', help = 'List todo tasks')
    parser.add_argument('-list-in-progress', action='store_true', help = 'List in progress tasks')

    args = parser.parse_args()
    
    if args.add != None:
        task_name = args.add
        task_add(task_name)

    elif args.update != None:
        task_id = int(args.update[0])
        new_description = args.update[1]
        task_update(task_id, new_description)

    elif args.delete != None:
        task_id = args.d
        task_delete(task_id)

    elif args.in_progress != None:
        task_id = args.in_progress
        task_in_progress(task_id)

    elif args.done != None:
        task_id = args.done
        task_done(task_id)    

    elif args.list_all:
        task_list_all()

    elif args.list_done:
        task_list_done()

    elif args.list_todo:
        task_list_todo()

    elif args.list_in_progress:
        task_list_in_progress()

if __name__ == '__main__':
    main()