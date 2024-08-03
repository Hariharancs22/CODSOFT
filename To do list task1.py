#CODSOFT tast1 - To Do List Application
def main():
    tasks = []

    while True:
        print("\n<<<<<<<<<<<<*\t To-Do List\t*>>>>>>>>>>>>")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove specific task")
        print("4. Mark task as DONE")
        print("5. Exit")

        choice = input("Enter your choice number:  ")

        #add
        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add ?:  "))
            
            for i in range(n_tasks):
                task = input("Enter the task:  ")
                tasks.append(task)
                print("Task added successfully!")

        #Show       
        elif choice == '2':
            print("The Entered tasks")
            for index, task in enumerate(tasks):
                print(index+1,'.', task)

        #remove        
        elif choice == '3':
            try:
                r_task = int(input("Enter the task number to remove: "))
                #task cannot be zero
                if 1 <= r_task <= len(tasks):
                    remove_task=tasks.pop(r_task - 1)
                    print("The task",remove_task, "is removed!")
                else:
                    print("\n Invalid task number.","\n Please check")
            except ValueError:
                print("Please enter a valid number.")
                print()

        #Mark as done        
        elif choice=='4':
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]
                tasks[task_num - 1] = (task, "Done")
                print(f"Task '{task}' marked as done.")
            else:
                print("Invalid task number.")        

        #exit                                
        elif choice == '5':
            print("Exiting the To-Do List Appliction.")
            print("\n THANK YOU")
            break

        else:
            print("Invalid choice. Please try again.")

#call the function            
if __name__ == "__main__":
    main()
