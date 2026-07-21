tasks =[]
print("Welcome to the to_Do tasks")
print("----------------------------------------")
while True :
    print("choose an option :")
    print("1: Added task")
    print("2: view tasks")
    print("3: Delete task")
    print("4: EXit")
    print("------------------------------------")
    choic = int(input("Enter your choic (1,4): "))
    if choic == 1:
        velue = input("Enter new task: ")
        tasks.append(velue)
        print("task add")
    elif choic == 2:
        if not tasks:
            print("no task yet")
        else :
            print("your tasks: ")
            i=1
            for Data in tasks:
                print(i,Data)
                i+=1
    elif choic == 3:
         if not tasks:
             print("no task yet")
         else:
             i=1
             for Data in tasks :
                 print(i,Data)
                 i+=1
             task_num = int(input("enter  task num  to Delete: "))
             if task_num>1 and task_num <=len(tasks):
                 Deletd= tasks.pop(task_num -1)
                 print(f"Deletd is :{Deletd}")
             else:
                 print(" Invalid value")
                 
    elif choic == 4:
          print("Good Bye!")
          break
                
             
                 
                 
                
        
        
