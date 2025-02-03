# CLI To Do List - User Guide

---

## Table of Contents

1. Overview
2. How to use the program

---

## Overview

The **CLI To Do List** is designed to allow users to create a 'To Do List'.  The is able to add tasks to a list and set a priority for each task.  The program has 6 options to choose from when using it:

1) Lets the user add new tasks to the 'To Do List'
2) Output the their current 'To Do List'
3) Allows the user to delete a task from their 'To Do List' by specifying the task number
4) Lists the users 'To Do List' in order of priority
5) Outputs the user's 'To Do List' to a JSON file
6) Exit the program

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

You will then see the 'To Do List' Configuraiton Menu and the 6 options described in the **Overview** section.

```python
╭────── Configuration Menu ──────╮
│                                │
│  --- John's To Do List ---     │
╰────────────────────────────────╯

1. Enter a new task
2. View Current To Do List
3. Remove task from To Do List
4. List taks in order of priority
5. Export 'To Do List' to JSON file
6. Exit

Select an option (1-6) [1/2/3/4/5/6]:

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
Your current 'To Do List' is as follows -

1. Eat Food

2. Drink Water

3. Play With Kids
```

---

### 2. View Current To Do List

If you select **2. View Current To Do List**, it outputs the same information as when you add a new task to your 'To Do List'.

```python
Your current 'To Do List' is as follows -

1. Eat Food

2. Drink Water

3. Play With Kids

4. Watch Tv

5. Do Homework
```

---

### 3. Remove Task From 'To Do List'

If you select **3. Remove Task From 'To Do List'**, it will ask you to provide the **task number** you would like to delete.  **DO NOT** provide your the priority number of your task.

```python
Enter the task number you would like to delete: 3
Task 3 has been successfully deleted
```
You input the task number and it will provide feedback stating that it has been successfully deleted.

If the task number is not in your 'To Do List', you will see the following output as an example.

```python
Task 3 does not exist
```

---

### 4. List Tasks In Order of Priority

If you select **4. List Tasks In Order of Priority**, it will output the tasks in your 'To Do List' in order of priority, instead of task number.

For instance, instead of seeing -

```python
Your current 'To Do List' is as follows -

1. Grocery Shopping

2. Laundry

3. Watch Tv
```

You will see them output in order of priority -

```python
Priority 1. Grocery Shopping
Priority 3. Laundry
Priority 10. Watch Tv
```


---

### 5. Export 'To Do List' to JSON File

If you select **5. Export 'To Do List' to JSON File**, your 'To Do List' will output to a JSON file in the same folder as **main.py** called **user_to_do_list.json**.

You will first see CLI output stating -

```python
Your 'To Do List' has been saved to a JSON file called 'user_to_do_list.json
```

Navigate to the same folder as the **main.py** file and open up your JSON file.  Your JSON file will appear as a normal JSON file such as the following -

```json
{
    "1": [
        "10",
        "eat food"
    ],
    "2": [
        "8",
        "drink water"
    ],
    "3": [
        "6",
        "play with kids"
    ],
    "4": [
        "4",
        "watch tv"
    ],
    "5": [
        "2",
        "do homework"
    ],
    "6": [
        "1",
        "go to sleep"
    ]
}
```

---

### 6. Exit

If you select **6. Exit**, you will see output similar to the one provided below in your CLI -

```python
Exiting your 'To Do List' Christian
```