#!/usr/bin/env python
# coding: utf-8

# In[2]:


# To-Do List

import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(title):
    task = {'title': title, 'status': 'incomplete'}
    tasks.append(task)
    save_tasks()

def list_tasks():
    for task in tasks:
        print(f"{task['title']} - {task['status']}")

if __name__ == "__main__":
    load_tasks()
    while True:
        action = input("Enter action (add/list/quit): ")
        if action == 'add':
            title = input("Enter task title: ")
            add_task(title)
        elif action == 'list':
            list_tasks()
        elif action == 'quit':
            break
        else:
            print("Unknown action.")

