# CLI app that lets users add , list, update, and delete to do tasks
# save the tasks in a local file - JSON , CSV, or SQLite
# command line parsing with argparse or third party libraries like click
# data persistence and CRUD operations
# basic user input validation and error handling

import sys
import json
import rich #import the rich module which is used to make the output look better
from rich import print #import the print function from the rich module
from rich.console import Console #import the Console class from the rich module
from rich.panel import Panel #import the Panel class from the rich module
from rich.table import Table #import the Table class from the rich module which is used to display data in a table format
from rich.prompt import Prompt #import the Prompt class from the rich module which is used to prompt the user for input

console = Console() #create a a Console class object called console
to_do_list = {} #create an empty dictionary called to_do_list
task_number = 0 #create a task number variable and set it to 0
name = "" #create a name variable and set it to an empty string


def main():

    global to_do_list #sets the to do list variable as a global variable that can be used as if it was in scope
    global task_number
    global name

    
    name = Prompt.ask("\nEnter your name").strip().lower().title() #asks the user for name.  strips any white space from the name and sets all characters to lower case and then sets the first letter of the name to upper case
    console.print("\n") #prints a new line
    
    while not name.isalpha(): #checks if the name is not all alphabetic characters
        console.print("Please enter a valid name\n") #prints a message to the user to enter a valid name
        name = Prompt.ask("\nEnter your name").strip().lower().title() #asks the user for name.  strips any white space from the name and sets all characters to lower case and then sets the first letter of the name to upper case 

    console.print(f"\nWelcome {name} to your 'To Do List!'\n") #prints a welcome message to the user with their name

    while True: #infinite loop that will continue until the user selects the exit option

        console.print(Panel(
            subtitle=f"[bold green]--- {name}'s 'To Do List' ---[/bold green]",
            title="[bold yellow]--- Configuration Menu --- [/bold yellow]",
            renderable="[bold white]\n1. Enter A New Task\n2. View Current 'To Do List'\n3. Delete Task From 'To Do List'\n4. View 'To Do List' Priority\n5. Export 'To Do List' to JSON File\n6. Load JSON File\n7. Exit [/bold white]")) #prints a panel with the configuration menu options.  uses title, subtitle, and renderable to display the menu.  Renderable is used to display the menu options.  The word renderable is used to display the menu options in a different color
        console.print("\n") #prints a new line

        choice = Prompt.ask("Select an option (1-7)", choices =[str(i) for i in range(1,8)]) #asks the user to input a number matching one of the 
        #above choices.  if it is not one of them, an error is thrown stating please select one of the available options. this is done via 'choices'
        console.print("\n") #prints a new line

        if choice == '1': #COMPLETED - #lets the user add a new task to the to do list
            priority = Prompt.ask("Enter your task priority (1-10) with 1 being the most important and 10 being the least", choices = [str(i) for i in range(1,11)],)
            #the above priority variable asks the user to input a number between 1 and 10.  if it is not one of them an error is thrown stating Please select one of the available options. this is done via 'choices'
            console.print("\n") #prints a new line
            task = Prompt.ask("Enter a description of your task") #asks the user to input a description of the task
            while not all(word.isalpha() for word in task.split()): #checks if all the words in the task are alphabetic characters
                console.print("Please enter a valid description of your task\n") #prints a message to the user to enter a valid task
                task = Prompt.ask("Enter a description of your task")
            console.print("\n") #prints a new line
            task_number += 1 #increments the task number by 1

            to_do_list[task_number] = [priority, task] #adds the task to the to do list with the task number as the key and the priority and task as the values

            to_do_list_table() #calls the to_do_list_table function to display the current to do list
            console.print("\n") #prints a new line


        elif choice == '2': #COMPLETED - outputs current to do list
            to_do_list_table() #calls the to_do_list_table function to display the current to do list

        elif choice == '3': #COMPLETED - lets the user delete a task from the to do list
            del_task() #calls the del_task function that is defined below

        elif choice == '4': #COMPLETED - lists tasks in order of priority
            to_do_list_priority_table() #calls the to_do_list_priority_table function that is defined below   
        
        elif choice == '5': #COMPLETED - exports to do list to JSON file
            create_json_file() #calls the create_json_file function that is defined below
            output_user_json_file() #calls the output_user_json_file function that is defined below

        elif choice == '6': #COMPLETED - loads a JSON file
            load_json_file() #calls the load_json_file function that is defined below

        elif choice == '7': #COMPLETED - exits the program
            print(f"Exiting your 'To Do List' {name}\n") #prints a message to the user that they are exiting the program
            exit() #exits the program

def del_task(): #COMPLETED - lets the user delete a task from the to do list
    task_deletion = Prompt.ask("Enter the task number you would like to delete. Total number of tasks -", choices = [str(num) for num in to_do_list.keys()]) #asks the user to input the task number they would like to delete
    console.print("\n") #prints a new line
    del to_do_list[int(task_deletion)] #deletes the task from the to do list
    console.print(f"Task {task_deletion} has been successfully deleted\n") #prints a message to the user that the task has been deleted
    to_do_list_table() #calls the to_do_list_table function to display the current to do list

def output_current_to_do_list(): #COMPLETED - outputs the current to do list
    console.print(f"Your current 'To Do List' is as follows -\n") #prints the current to do list
    count = 1 #count variable to increment the number of tasks
    for value in to_do_list.values(): #iterates through the values of the to do list
        console.print(f"{count}. {value[1].title()}\n") #prints the task with the count in front of it.  uses title to capitalize the first letter of each word
        count += 1 #increments the count by 1

def create_json_file(): #function to create a JSON file
    user_json_file = json.dumps(to_do_list, indent=4) #converts the to do list to a JSON file with an indent of 4

def output_user_json_file(): #function to output the JSON file
    console.print(f"Your 'To Do List' has been saved to a JSON file called 'user_to_do_list.json'\n") #prints a message to the user that the to do list has 
    #been saved to a JSON file
    with open("user_to_do_list.json", "w") as file: #opens the JSON file in write mode because we are writing to it and sets it as a variable called file
        json.dump(to_do_list, file, indent=4) #writes the to do list to a JSON file with an indent of 4 because it is easier to read

def load_json_file(): #function to load a previous JSON file or JSON file to use in the 'To Do List' python program
    global to_do_list #sets the to do list variable as a global variable that can be used as if it was in scope
    with open("user_to_do_list.json", "r") as file: #opens the JSON file in read mode
        to_do_list = json.load(file) #loads the JSON file into the to do list variable

def to_do_list_table(): #function to display the current to do list in a table format
    global name #sets the name variable as a global variable that can be used as if it was in scope
    table = Table(title = name + "'s 'To Do List'", title_style="bold pink", style="magenta", show_lines=True) #creates a table with the title of the user's name and To Do List

    table.add_column("Task Number", justify="center", header_style="bold white", style="cyan", no_wrap=True) #adds a column to the table with the header of Task Number
    table.add_column("Priority", justify="center", header_style="bold white", style="red", no_wrap=True) #adds a column to the table with the header of Priority
    table.add_column("Task", justify="center", header_style="bold white", style="green", no_wrap=True) #adds a column to the table with the header of Task

    for key, value in to_do_list.items(): #iterates through the to do list key value pairs.  key is the task number and value is the priority and task
        table.add_row(str(key), str(value[0]), str(value[1].title())) #we use str() to conver the key and value to a string because the table.add_row() function only accepts strings

    console.print(table, "\n") #prints the table with a new line

def to_do_list_priority_table():
    global name #sets the name variable as a global variable that can be used as if it was in scope
    global to_do_list #sets the to do list variable as a global variable that can be used as if it was in scope

    console.print(f"Your current 'To Do List' in order of priority is as follows -\n") #prints the current to do list in order of priority
    count = 1 #count variable to increment the number of tasks
    
    sorted_tasks = sorted(to_do_list.items(), key=lambda item: int(item[1][0])) #sorts the to do list by the priority of the task
        #key=lambda item: int(item[1][0]) is a lambda function that takes in an item and returns the integer of the priority of the task.  
        #it sets the priority, starting at 1, outputs the task and then increments the priority by 1
    
    table = Table(title = name + "'s 'To Do List'", title_style="bold pink", style="magenta", show_lines=True) #creates a table with the title of the user's name and To Do List

    table.add_column("Task Number", justify="center", header_style="bold white", style="cyan", no_wrap=True) #adds a column to the table with the header of Task Number
    table.add_column("Priority", justify="center", header_style="bold white", style="red", no_wrap=True) #adds a column to the table with the header of Priority
    table.add_column("Task", justify="center", header_style="bold white", style="green", no_wrap=True) #adds a column to the table with the header of Task
    
    for task in sorted_tasks: #iterates through the sorted tasks variable
        table.add_row(str(count), str(task[1][0]), str(task[1][1].title())) #adds the task to the table with the count in front of it.  uses title
        count += 1 #increments the count by 1
    
    console.print(table, "\n") #prints a new line

if __name__ == "__main__": #checks if the script is being run directly
    main() #calls the main function to run the program
