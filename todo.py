#!/usr/bin/python3
import datetime
import os
import sys

fileName = os.path.join(os.getcwd(), "todo.txt")
doneFileName = os.path.join(os.getcwd(), "done.txt")

open(fileName, 'a').close()
open(doneFileName, 'a').close()

if __name__ == "__main__":
    args = sys.argv
    helpString = f'''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''
    if len(args) <= 1:
        print("Usage :-")
        print('$ ./todo add "todo item"  # Add a new todo')
        print('$ ./todo ls               # Show remaining todos')
        print('$ ./todo del NUMBER       # Delete a todo')
        print('$ ./todo done NUMBER      # Complete a todo')
        print('$ ./todo help             # Show usage')
        print('$ ./todo report           # Statistics')
    else:
        if "help" in args and len(args) < 3:
            print(helpString)
        else:
            with open(fileName, 'r+') as task, open(doneFileName, 'r+') as done:
                tasks = task.readlines()
                doneTasks = done.readlines()
                totalTasks = len(tasks)
                doneTasksCount = len(doneTasks)

                if args[1] == "ls":
                    if totalTasks < 1:
                        print("There are no pending todos!")
                    for i in range(-1, -totalTasks - 1,-1):
                        tasks[i] = tasks[i].replace("\n", '')
                        print(f"[{totalTasks + i + 1}] {tasks[i]}")

                elif args[1] == "report":
                    print(f"{datetime.date.today()} Pending : {totalTasks} Completed : {doneTasksCount}")

                elif args[1] == "add":
                    try:
                        taskName = args[2]
                        task.write(f"{taskName}\n")
                        print(f'Added todo: "{taskName}"')
                    except IndexError:
                        print("Error: Missing todo string. Nothing added!")

                elif args[1] == 'del':
                    try:
                        number = int(args[2])
                        if number > totalTasks or number < 1:
                            print(f"Error: todo #{number} does not exist. Nothing deleted.")
                        else:
                            tasks.remove(tasks[number - 1])
                            task.seek(0)
                            task.truncate(0)
                            for i in tasks:
                                task.write(i)
                            print(f"Deleted todo #{number}")
                    except IndexError:
                        print("Error: Missing NUMBER for deleting todo.")

                elif args[1] == "done":
                    try:
                        number = int(args[2])
                        if number > totalTasks or number < 1:
                            print(f"Error: todo #{number} does not exist.")
                        else:
                            doneTask = tasks[number - 1]
                            tasks.remove(doneTask)
                            done.read()
                            done.write(f"x {datetime.date.today()} {doneTask}")
                            task.seek(0)
                            task.truncate(0)
                            for i in tasks:
                                task.write(i)
                            print(f"Marked todo #{number} as done.")
                    except IndexError:
                        print("Error: Missing NUMBER for marking todo as done.")
