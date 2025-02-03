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
from rich.prompt import Prompt #import the Prompt class from the rich module

console = Console() #create a a Console class object called console
to_do_list = {} #create an empty dictionary called to_do_list
task_number = 0 #create a task number variable and set it to 0


def main():

    global to_do_list #sets the to do list variable as a global variable that can be used as if it was in scope
    global task_number

    
    name = Prompt.ask("\nEnter your name").lower().title() #asks the user for name.  sets all characters to lower case and then sets the first 
    #character to uppercase via title
    console.print(f"\nWelcome {name} to your 'To Do List'\n") #prints a welcome message to the user with their name

    while True: #infinite loop that will continue until the user selects the exit option

        console.print(Panel.fit(f"\n[bold green]--- {name}'s To Do List ---[/bold green]",title="Configuration Menu", )) #creates a box with Configuration Menu 
        #at the top.  In the center is displayed the user's name and To Do List
        console.print("\n1. Enter a new task\n2. View Current To Do List\n3. Remove task from To Do List\n4. List taks in order of priority\n5. Export 'To Do List' to JSON file\n6. Exit\n") #asks the user what they want to do

        choice = Prompt.ask("Select an option (1-6)", choices =[str(i) for i in range(1,7)]) #asks the user to input a number matching one of the 
        #above choices.  if it is not one of them an error is thrown stating Please select one of the available options. this is done via 'choices'
        console.print("\n") #prints a new line

        if choice == '1': #COMPLETED - #lets the user add a new task to the to do list
            priority = Prompt.ask("Enter your task priority (1-10) with 1 being the most important and 10 being the least", choices = [str(i) for i in range(1,11)],)
            #the above priority variable asks the user to input a number between 1 and 10.  if it is not one of them an error is thrown stating Please select one of the available options. this is done via 'choices'
            console.print("\n") #prints a new line
            task = Prompt.ask("Enter a description of your task") #asks the user to input a description of the task
            console.print("\n") #prints a new line
            task_number += 1 #increments the task number by 1

            to_do_list[task_number] = [priority, task] #adds the task to the to do list with the task number as the key and the priority and task as the values

            output_current_to_do_list() #calls the output_current_to_do_list function to display the current to do list
            console.print("\n") #prints a new line


        elif choice == '2': #COMPLETED - outputs current to do list
            output_current_to_do_list()

        elif choice == '3': #COMPLETED - lets the user delete a task from the to do list
            del_task() #calls the del_task function that is defined below

        elif choice == '4': #COMPLETED - lists tasks in order of priority
            console.print(f"Your current 'To Do List' in order of priority is as follows -\n") #prints the current to do list in order of priority
            count = 1 #count variable to increment the number of tasks
            list_length = len(to_do_list) #gets the length of the to do list, not currently used
            
            sorted_tasks = sorted(to_do_list.items(), key=lambda item: int(item[1][0])) #sorts the to do list by the priority of the task
                #key=lambda item: int(item[1][0]) is a lambda function that takes in an item and returns the integer of the priority of the task.  
                #it sets the priority, starting at 1, outputs the task and then increments the priority by 1
            for task in sorted_tasks: #iterates through the sorted tasks variable
                console.print(f"Priority {task[1][0]}. {task[1][1].title()}") #prints the task with the priority in front of it.  uses title 
                #to capitalize the first letter of each word
            console.print("\n") #prints a new line    
        
        elif choice == '5': #COMPLETED - exports to do list to JSON file
            create_json_file() #calls the create_json_file function that is defined below
            output_user_json_file() #calls the output_user_json_file function that is defined below

        elif choice == '6': #COMPLETED - exits the program
            print(f"Exiting your 'To Do List' {name}\n") #prints a message to the user that they are exiting the program
            exit() #exits the program

def del_task(): #COMPLETED - lets the user delete a task from the to do list
    task_deletion = Prompt.ask("Enter the task number you would like to delete\n") #asks the user to input the task number they would like to delete
    if int(task_deletion) in to_do_list: #checks if the task number is in the to do list
        del to_do_list[int(task_deletion)] #deletes the task from the to do list
        console.print(f"Task {task_deletion} has been deleted\n") #prints a message to the user that the task has been deleted
    else: #if the task number is not in the to do list
        console.print(f"Task {task_deletion} does not exist\n") #prints a message to the user that the task does not exist
    output_current_to_do_list() #calls the output_current_to_do_list function to display the current to do list

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
    with open("user_to_do_list.json", "w") as file:
        json.dump(to_do_list, file, indent=4) #writes the to do list to a JSON file with an indent of 4

main()
