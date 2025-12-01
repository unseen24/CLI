# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import argparse
import json
import datetime

#move this somewhere else later
tasks = {
        'id': 0,
        'description': '',
        'status': '',
        'createdAt': '',
        'updatedAt': ''
    }

def taskAdd(task_name):
#check if task name already exists and if json file exists
#create json file if it doesn't exist, with an empty dictionary the value must be a list of dictionaries
#open json file check what number of id
#increment id by 1 for new task
#add the task in a dictionary
# add the dictionary to the list of dictionaries in the json file

    tasks.update({'description': task_name, 'createdAt': datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")})
    with open('tasks.json', 'a+') as f:
        data = json.load(f)
        data["tasks"].append(tasks)
        f.seek(0)
        json.dump(data, f)
    print('Task Added Successfully')

def taskUpdate():
    pass

def taskDelete():
    pass

def taskInProgress():
    pass

def taskDone():
    pass   

def taskListAll():
    pass

def taskNotDone():
    pass

def taskMark():
    pass

def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    parser.add_argument('-a', type = str, metavar = '[Task Name]', default = None, help = 'Add a new task')
    
    args = parser.parse_args()
    
    if args.a != None:
        task_name = args.a
        taskAdd(task_name)

    with open('tasks.json') as f:
        data = json.load(f)
        
    print(data.get('id'))

if __name__ == '__main__':
    main()