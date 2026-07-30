for x in range(5):
    print("mimo")
    
for y in range(10):
    print(y)
for b in range(1,11):
    print(b)
for w in range(2,10,2):
    print(w)
    
couler=["red","Blue","green"]
for x in couler:
    print(x)
    
name="mimo"
for i in name:
    print(i.upper())
    
colour =["red","blue","Bink"]
for i in colour:
   if i =="Bink":
     print(f"my fovirt colour is {i} ")
        
   else:
       print(i)
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if i==2:
        print(f"my fovrite num {i}")
    else:
        print(i)
        
number =[1,2,3,4,5,6,7,8,9,10]
for i in number:
    if i %2==0:
        print(f"\n{i}")
print("\n finishd the loop succes fully")

attendees =["Roky","Bob","Xyla"]
for person in attendees:
    print(person)
    print("Attendance confirmed!")
    print("--------------------------------")
print("finished")

name=["Xyle","omer","mustafa","khald"]
for i in name:
    print(i)
    person=input("is this persons attending?(yes/no)\n")
    if person=="yes":
        print("Attendance confirmed!")
        print("------------------------------")
    else:
        print("Attendance not confirmed!")
print("-----------------------")


Attend=input("Enter the name of attends separted commas: ")
Attend_input =Attend.split(", ")
for i in Attend_input:
    print("\n" + i + "\n")
    name=input("is this person attending?(yes/no)\n")
    if name =="yas":
        print("Attendans confirmed!")
        print("-----------------------------")
    else:
        print("Attendans not confirmed!")
    print("-----------------------------")

    
traval=input("please type the name countries: ").split(", ")
for i in traval:
    print(f"\n{i}\n")
    name=input(f"have you ever visidet{i} befor?!(yes/no)").lower()
    if name =="yas":
        print("i hope you had a wonder full!\n")
    else:
        print("I hope you get to visit!\n")

print("______welcome to-do list tasks________ ")
tasks=input("Enter your tasks for today: \n ").split(", ")
done_tasks=[]#مهمات تم فعلها
onGoing_tasks=[]#لم يتم فعلها
for task in tasks:
    print(f"\n{task}\n")
    done=input(f"Did you finish {task} alredy?(yes/no)\n").lower()
    
    if done =="yas":
        print("nise Job!")
        done_tasks.append(task)
    else:
        print("Try not to put it off!!!")
        onGoing_tasks.append(task)
    print("|--------------------------|")
see_progress=input("Do You want see Your todays progress?(yes/no)\n")
if see_progress=="no":
    input("ohh!ok")
else:
    print("|-------------|\n")
    print(done_tasks)
    print("|-------------|\n")
    print(onGoing_tasks)
    
       
        
#range
#range(start),range(start,stop),range(start,stop,step)
print("---Welcome to the multiplication---")
num=int(input("Enter a Number: \n"))
print(f"\nmultipliction:{num}")
for i in range(1,11):
    result=num*i
    print(f"{num}*{i}={result}") 
        
        
    

    
        
    
   
    



    

























         
        
    
