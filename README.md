# CLI To Do List - User Guide

---

## Table of Contents

1. Overview
2. How to use the program

---

## Overview

The **CLI To Do List** is designed to allow users to create a 'To Do List'.  The user is able to add tasks to a list and set a priority for each task.  The program has 9 options to choose from when using it:

1) Enter A New Task
2) View Current 'To Do List'
3) Delete Task From 'To Do List'
4) Update Task In 'To Do List'
5) Update Task Priority
6) View 'To Do List' Priority
7) Export 'To Do List' to JSON File
8) Load JSON File
9) Exit

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
│                                                                                                                                                                    │ 
│ 1. Enter A New Task                                                                                                                                                │ 
│ 2. View Current 'To Do List'                                                                                                                                       │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                   │ 
│ 4. Update Task In 'To Do List'                                                                                                                                     │ 
│ 5. Update Task Priority                                                                                                                                      │ 
│ 6. View 'To Do List' Priority                                                                                                                                │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                  │ 
│ 8.Load JSON File
 │ 9. Exit                                                                                                                                                           │ 
└─────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8]:

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
│ Task Number │ Priority │    Task     │
├─────────────┼──────────┼─────────────┤
│      1      │    1     │  Eat Food   │
├─────────────┼──────────┼─────────────┤
│      2      │    2     │ Drink Water │
├─────────────┼──────────┼─────────────┤
│      3      │    3     │ Do Homework │
└─────────────┴──────────┴─────────────┘
```

---

### 2. View Current To Do List

If you select **2. View Current To Do List**, it outputs the same information as when you add a new task to your 'To Do List'.

```python
         Bob's 'To Do List'
┌─────────────┬──────────┬─────────────┐
│ Task Number │ Priority │    Task     │
├─────────────┼──────────┼─────────────┤
│      1      │    1     │  Eat Food   │
├─────────────┼──────────┼─────────────┤
│      2      │    2     │ Drink Water │
├─────────────┼──────────┼─────────────┤
│      3      │    3     │ Do Homework │
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
│ Task Number │ Priority │    Task     │
├─────────────┼──────────┼─────────────┤
│      1      │    1     │  Eat Food   │
├─────────────┼──────────┼─────────────┤
│      2      │    2     │ Drink Water │
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

### 5. Update Task Priority

If you select **5. Update Task Priority**, it will allow you to update the priority of you chosen task.  See the example below -

```python
           Bob's 'To Do List'
┌─────────────┬──────────┬──────────────┐
│ Task Number │ Priority │     Task     │
├─────────────┼──────────┼──────────────┤
│      1      │    1     │ Go For A Run │
└─────────────┴──────────┴──────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 5


Enter the task number you would like to update. Total number of tasks - [1]: 1


Enter the new priority of your task [1/2/3/4/5/6/7/8/9/10]: 10


┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 2


           Bob's 'To Do List'
┌─────────────┬──────────┬──────────────┐
│ Task Number │ Priority │     Task     │
├─────────────┼──────────┼──────────────┤
│      1      │    10    │ Go For A Run │
└─────────────┴──────────┴──────────────┘
```


---

### 6. View 'To Do List' Priority

If you select **6. View 'To Do List' Priority**, you will be provided your 'To Do List' in order of priority from 1 to 10, rather than in the order of task number.  See an example below.

```python

            Bob's 'To Do List'
┌─────────────┬──────────┬────────────────┐
│ Task Number │ Priority │      Task      │
├─────────────┼──────────┼────────────────┤
│      1      │    10    │  Go For A Run  │
├─────────────┼──────────┼────────────────┤
│      2      │    5     │    Eat Food    │
├─────────────┼──────────┼────────────────┤
│      3      │    6     │  Drink Water   │
├─────────────┼──────────┼────────────────┤
│      4      │    2     │    Watch Tv    │
├─────────────┼──────────┼────────────────┤
│      5      │    1     │ Play With Kids │
└─────────────┴──────────┴────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 6


Your current 'To Do List' in order of priority is as follows -

            Bob's 'To Do List'
┌─────────────┬──────────┬────────────────┐
│ Task Number │ Priority │      Task      │
├─────────────┼──────────┼────────────────┤
│      1      │    1     │ Play With Kids │
├─────────────┼──────────┼────────────────┤
│      2      │    2     │    Watch Tv    │
├─────────────┼──────────┼────────────────┤
│      3      │    5     │    Eat Food    │
├─────────────┼──────────┼────────────────┤
│      4      │    6     │  Drink Water   │
├─────────────┼──────────┼────────────────┤
│      5      │    10    │  Go For A Run  │
└─────────────┴──────────┴────────────────┘

```

---

### 7. Export 'To Do List' to JSON File

If you select **7. Export 'To Do List' to JSON File**, you will see output stating that **"Your 'To Do List' has been saved to a JSON file called 'user_to_do_list.json"**.  See example below -

```python

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 7


Your 'To Do List' has been saved to a JSON file called 'user_to_do_list.json'
```

---

### 8. Load JSON File

If you select **8. Load JSON File**, the program will load a JSON file as your 'To Do List'.  It is imperative that the file be named **user_to_do_list.json** in order for it to work correctly.  This ensures file consistency when the user exports the 'To Do List' and loads it back into the program.  See example below -

```python
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 8


Your 'To Do List' has been loaded from the JSON file called 'user_to_do_list.json'
```

---

### 9. Exit

If you select **9. Exit**, your 'To Do List' will be default exported to the a JSON file called **user_to_do_list.json**.  This is to ensure that the user does not lose the data that is in their 'To Do List' inadvertently.  Example output below -

```python
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Configuration Menu ---  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ 
│                                                                                                                                                                                                                                                                                                                                         │ 
│ 1. Enter A New Task                                                                                                                                                                                                                                                                                                                     │ 
│ 2. View Current 'To Do List'                                                                                                                                                                                                                                                                                                            │ 
│ 3. Delete Task From 'To Do List'                                                                                                                                                                                                                                                                                                        │ 
│ 4. Update Task In 'To Do List'                                                                                                                                                                                                                                                                                                          │ 
│ 5. Update Task Priority                                                                                                                                                                                                                                                                                                                 │ 
│ 6. View 'To Do List' Priority                                                                                                                                                                                                                                                                                                           │ 
│ 7. Export 'To Do List' to JSON File                                                                                                                                                                                                                                                                                                     │ 
│ 8. Load JSON File                                                                                                                                                                                                                                                                                                                       │ 
│ 9. Exit                                                                                                                                                                                                                                                                                                                                 │ 
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── --- Bob's 'To Do List' --- ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 


Select an option (1-9) [1/2/3/4/5/6/7/8/9]: 9


Your 'To Do List' has been saved to a JSON file called 'user_to_do_list.json'

If you want to load this 'To Do List' in the future, select option 8 from the menu

Exiting your 'To Do List' Bob
```
