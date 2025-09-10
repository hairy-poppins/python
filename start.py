#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def addTask(taskNum, tasks):
  t = input("Title of New Task: ")
  while True:
    p = float(input("Prioity Ranking (0.0-5.0): "))
    if 0.0 > p or p > 5.0:
      print("Please use a number between 0.0 and 5.0")
    else: 
      break
      

  tasks.append({
        "number": taskNum,
        "task": t,
        "complete": False,
        "priority": p
    })
  
  
tasks = []
stop = True
task_num = 1
while True:
  print('\033[1m**To Do List Options**\033[0m\n1 - Add task \n2 - View list \n3 - Edit a task\n4 - View Sorted List\n5 - Exit\n')
  response = input("Choice: ")
  
  ##ADD TASK
  if response == "1":
    addTask(task_num, tasks)
    task_num += 1
    while stop:
      response1 = input("New Task? (y/n)  -  ")
      if response1 == "y":
        addTask(task_num, tasks)
        task_num += 1
      elif response1 == "n":
        stop = False
      else:
        print("Please use y/n")

  ##VIEW TASKS
  elif response == "2":
    for task in tasks:
      status = '✅ Done' if task['complete'] else '❌ Uncomplete'
      print(f"{task['number']}. {task['task']} (Priority: {task['priority']}) - {status}")
  
  ##EDIT TASKS
  elif response == "3":
    response3 = int(input("Which task number would you like to update?"))
    task = tasks[response3-1]
    print(f"{task['number']}. {task['task']} - {'✅ Done' if task['complete'] else '❌ Uncomplete'}")

    update_choice = input("Edit title (t), mark as complete (m), or delete task (x)")
    if update_choice == "t":
      task["task"] = input("New title name: ")
    elif update_choice == "m":
      task["complete"] = True
    elif update_choice == "x":
      del tasks[response3-1]
      for idx, task in enumerate(tasks, start=1):
          task["number"] = idx
      task_num = len(tasks) + 1 
    else:
      print("Please use 't', 'm', or 'x'")

  ##SORTED TASKS
  elif response == "4":
    sorted_tasks = sorted(tasks, key=lambda task: task['priority'], reverse=True)
    print("**Tasks Sorted by Priority**")
    for task in sorted_tasks:
        status = '✅ Done' if task['complete'] else '❌ Uncomplete'
        print(f"{task['number']}. {task['task']} (Priority: {task['priority']}) - {status}")
  elif response == "5":
    break



    
      
    

  






