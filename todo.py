tasks=[]
while True:
    print("--------To Do List--------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if(choice=='1'):
        task=input("Enter Task: ")
        tasks.append(task)
        print("Task Added!")
    elif(choice=='2'):
        if(len(tasks)==0):
            print("Task List is Empty!")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
    elif(choice=='3'):
        num=int(input("Enter the task number to delete: "))
        if(1<=num<=len(tasks)):
            tasks.pop(num-1)
        else:
            print("Invalid number!")
    elif(choice=='4'):
        print("All set! Catch you later!")
        break
    else:
        print("Invalid choice")
     
    