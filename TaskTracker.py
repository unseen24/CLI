# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import argparse
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

            json_file["tasks"].append(
                {
                'id': json_file["tasks"][-1].get('id')+1,
                'description': task_name,
                "status": "",
                'createdAt': datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                "updatedAt": ""
                    }
            )
        
        with open('tasks.json', 'w') as f:
            json.dump(json_file, f, indent=4)

    else:
        json_data = {
            "tasks": [
                {
                    "id": 1,
                    "description": task_name, 
                    "status": "",
                    "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"),
                    "updatedAt": ""
                    }
                ]
        }
        with open('tasks.json', 'w') as f:
            json.dump(json_data, f, indent=4)



    
def task_update():
    pass

def task_delete():
    pass

def task_in_progress():
    pass

def task_done():
    pass   

def task_list_all():
    pass

def task_not_done():
    pass

def task_mark():
    pass

def main():
#wont run if json has errors
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    parser.add_argument('-a', type = str, metavar = '[Task Name]', default = None, help = 'Add a new task')
    
    args = parser.parse_args()
    
    if args.a != None:
        task_name = args.a
        task_add(task_name)

if __name__ == '__main__':
    main()