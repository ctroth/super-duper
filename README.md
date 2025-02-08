# CLI To Do List - User Guide

---

## Table of Contents

1. Overview
2. How to use the program

---

## Overview

The **CLI To Do List** is designed to allow users to create a 'To Do List'.  The is able to add tasks to a list and set a priority for each task.  The program has 8 options to choose from when using it:

1) Enter A New Task
2) View Current 'To Do List'
3) Delete Task From 'To Do List'
4) Update Task In 'To Do List'
5) View 'To Do List' Priority
6) Export 'To Do List' to JSON File
7) Load JSON FIle
8) Exit

---

## How to Use the Program


To start the 'CLI To Do List' using the termianl enter the following command -

```bash
python main.py
```

You will then be prompted to enter your first name and will see the following output -

```python
Enter your name:
Welcome " " to your 'To Do List'
```

You will then see the 'To Do List' Configuraiton Menu and the 8 options described in the **Overview** section.

```python
┌─────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                        │ 
│ 1. Enter A New Task                                                                                                                                                │ 
│ 2. View Current 'To Do List'                                                                                                                                       │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                   │ 
│ 4. Update Task In 'To Do List'                                                                                                                                     │ 
│ 5. View 'To Do List' Priority                                                                                                                                      │ 
│ 6. Export 'To Do List' to JSON File                                                                                                                                │ 
│ 7. Load JSON File                                                                                                                                                  │ 
│ 8. Exit                                                                                                                                                            │ 
└─────────────────────────────────────────────────────────────────── --- Chris's 'To Do List' --- ───────────────────────────────────────────────────────────────────┘ 


Select an option (1-8) [1/2/3/4/5/6/7/8]:

```

--- 

### 1. Enter a new task

If you select -  **1. Enter a new task** - you will see the following options in order -

```python
Enter your task priority (1-10) with 1 being the most important and 10 being the least [1/2/3/4/5/6/7/8/9/10]:
```

Followed by -

```python
Enter a description of your task:
```

The instructions are straight forward.  Enter a prioroity number for the task you want to add and then add in the task you want in your to do list.  Everytime you enter a new task to the 'To Do List' you will see the current version of your 'To Do List' output to your CLI.

An example of a 'To Do List' -

```python
         Bob's 'To Do List'
┌─────────────┬──────────┬─────────────┐
│ Task Number│ Priority│    Task    │
├─────────────┼──────────┼─────────────┤
│      1     │    1    │  Eat Food  │
├─────────────┼──────────┼─────────────┤
│      2     │    2    │ Drink Water│
├─────────────┼──────────┼─────────────┤
│      3     │    3    │ Do Homework│
└─────────────┴──────────┴─────────────┘
```

---

### 2. View Current To Do List

If you select **2. View Current To Do List**, it outputs the same information as when you add a new task to your 'To Do List'.

```python
         Bob's 'To Do List'
┌─────────────┬──────────┬─────────────┐
│ Task Number│ Priority│    Task    │
├─────────────┼──────────┼─────────────┤
│      1     │    1    │  Eat Food  │
├─────────────┼──────────┼─────────────┤
│      2     │    2    │ Drink Water│
├─────────────┼──────────┼─────────────┤
│      3     │    3    │ Do Homework│
└─────────────┴──────────┴─────────────┘
```

---

### 3. Delete  Task From 'To Do List'

If you select **3. Remove Task From 'To Do List'**, it will ask you to provide the **task number** you would like to delete.  **DO NOT** provide your the priority number of your task.

```python
Enter the task number you would like to delete. Total number of tasks - [1/2/3]:
Task 3 has been successfully deleted

          Bob's 'To Do List'
┌─────────────┬──────────┬─────────────┐
│ Task Number│ Priority│    Task    │
├─────────────┼──────────┼─────────────┤
│      1     │    1    │  Eat Food  │
├─────────────┼──────────┼─────────────┤
│      2     │    2    │ Drink Water│
└─────────────┴──────────┴─────────────┘
```
You input the task number and it will provide feedback stating that it has been successfully deleted.

If the task number is not in your 'To Do List', you will see the following output as an example.

```python
Enter the task number you would like to delete. Total number of tasks - [1/2]: 3
Please select one of the available options
Enter the task number you would like to delete. Total number of tasks - [1/2]:
```

---

### 4. Update Task in 'To Do List'

If you select **4. Update Task in 'To Do List'**, it will ask you to enter the task number you would like to update as seen in the below output -

```python
Enter the task number you would like to update.  Total number of tasks - [1]:
```

It will then prompt y ou to enter the new description of your task as seen in the below output -

```python
Enter the new description of your task:
```

Upon entering a new task description it will take you back to the main **Configuration Menu** screen.


---

### 5. View 'To Do List' Priority

If you select **5. View 'To Do List' Priority', it will output your 'To Do List' in order of priority, rather than in the order that you input them in (task number).  Using the task list we created previously, we had selected 'Eat Food' as priority 1 in our list.  We then updated it to 'Go For A Run -

```python

```

---

### 6. Export 'To Do List' to JSON File


---

### 7. Load JSON File


---

### 8. Exit

If you select **6. Exit**, you will see output similar to the one provided below in your CLI -

```python
Exiting your 'To Do List' Christian
```