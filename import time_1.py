import time
print("___⏳ welcome too the promodoro timers___")
#اولا: ادخال عدد الدقايق
minutes = int(input("Enter time in minutes:"))
#*60
total = minutes*60
while total<0:
   minutes = total//60
   secs = total %60
   clock =f"{minutes:02d}:{secs:02d}"
   print(f"\r time remai ninig :{clock}",end="")
   time.sleep(1)
   total-=1
   
   print("\n⏳times up,take a Braek ") 
    




