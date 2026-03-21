def task():
    tasks = [] #empty list
    print("Welcome to the task manager!")

    total_tasks = int(input("Enter how many tasks do you want to add = "))
    for i in range(1, total_tasks+1):
        tasks_name = input(f"Enter the name of task {i} = ")
        tasks.append(tasks_name) 

        print(f"Todays tasks are:\n{tasks}")

        while True:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
            if operation == 1:
                add = input ("Enter the name of task you want to add = ")
                tasks.append(add)
                print(f"Task {add} has been added successfully!")

            elif operation == 2:
                    updated_val = input("Enter the name of task you want to update = ")
                    if updated_val in tasks:
                         up = input("Enter new task = ")
                         ind = tasks.index(updated_val)
                         tasks[ind] = up
                         print(f"Task {updated_val} has been updated to {up}!")

                    elif operation == 3:
                            del_val = input("Which task you want to delete = ")
                            if del_val in tasks:
                                 ind = tasks.index(del_val)
                                 del tasks[ind]
                                 print(f"Task {del_val} has been deleted successfully!")

                    elif operation == 4:
                            print(f"Todays tasks are:\n{tasks}")

                    elif operation == 5:
                            print("Exiting the task manager. Goodbye!")
                            break
                    
                    else:
                            print("Invalid operation. Please try again.")

task()