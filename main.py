# CLI app that lets users add , list, update, and delete to do tasks
# save the tasks in a local file - JSON , CSV, or SQLite
# command line parsing with argparse or third party libraries like click
# data persistence and CRUD operations
# basic user input validation and error handling

import sys
import json
import rich
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console() #create a a Console class object called console
to_do_list = {}
task_number = 0


def main():

    global to_do_list #sets the to do list variable as a global variable that can be used as if it was in scope
    global task_number

    
    name = Prompt.ask("Enter your name").lower().title() #asks the user for name.  sets all characters to lower case and then sets the first character to uppercase via title
    
    while True:

        console.print(Panel.fit(f"\n[bold green]--- {name}'s To Do List ---[/bold green]",title="Configuration Menu", )) #creates a box with Configuration Menu at the top.  In the center is displayed the user's name and To Do List
        console.print("1. Enter a new task\n2. View Current To Do List\n3. Remove task from To Do List\n4. List taks in order of priority\n5. Export 'To Do List' to JSON file\n6. Exit\n") #asks the user what they want to do

        choice = Prompt.ask("Select an option (1-6)", choices =[str(i) for i in range(1,7)]) #asks the user to input a number matching one of the above choices.  if it is not one of them an error is thrown stating Please select one of the available options. this is done via 'choices'

        if choice == '1': #COMPLETED
            priority = Prompt.ask("Enter your task priority (1-10) with 1 being the most important and 10 being the least", choices = [str(i) for i in range(1,11)],)
            task = Prompt.ask("Enter a description of your task")
            task_number += 1

            to_do_list[task_number] = [priority, task]

            console.print(f"Your current 'To Do List' is as follows -\n")
            for value in to_do_list.values():
                console.print(value[1])
            console.print("\n")


        elif choice == '2': #COMPLETED
            console.print(f"Your current 'To Do List' is as follows -\n")
            count = 1
            for value in to_do_list.values():
                console.print(f"{count}. {value[1].title()}\n")
                count += 1

        elif choice == '3':
            pass

        elif choice == '4':
            console.print(f"Your current 'To Do List' in order of priority is as follows -\n")
            count = 1
            list_length = len(to_do_list)
            
            while count < list_length:
                for value in to_do_list.values(): #value[0] is listed as a string
                    if value[int(0)] == count:
                        console.print(f"Priority {count}. {value[1]}")
                        count += 1
                
        
        elif choice == '5':
            pass

        elif choice == '6': #COMPLETED
            exit()
        
        print(f"Exiting your 'To Do List'...")

main()
