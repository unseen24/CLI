# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

import argparse
import json
import os

def taskAdd():
    '''create json file here with:
        id: A unique identifier for the task
        description: A short description of the task
        status: The status of the task (todo, in-progress, done)
        createdAt: The date and time when the task was created
        updatedAt: The date and time when the task was last updated 
'''
    tasks = {
        'id': 1,
        'description': '',
        'status': '',
        'createdAt': '',
        'updatedAt': ''
    }
#if file doest not exist, create file
    if not os.path.exists('tasks.json'):


        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)

        print('File created. Task Added Successfully')
#if file exist, open file and append new task
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

    parser.add_argument('-a', type = str, nargs = '+', metavar = 'taskAdd', default = None, help = 'Add a new task')
    args = parser.parse_args()