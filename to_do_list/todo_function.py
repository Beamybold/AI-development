"""
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

#add tasks
tasks = []
# tasks = input("Enter your tasks: ")


def add_task(task): #Function to add a task
    tasks.append(task)
    print(f"New task added: {tasks}")


def remove_task(task): #function to remove a task from the list
    if task in tasks:
        tasks.remove(tasks)
        print(f"Removedd Task: {task}")
    else:
        print("task unfound!")

def completed_tasks(task): #function to show completed tasks
    for tasks in tasks:
        if task == "completed":
            print(f"Task '{task}' completed ")
        else:
            print("Task uncompleted!")

def view_tasks(): #function to display tasks
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1): #start numbering from 1
            print(f"{i}. {task}")



