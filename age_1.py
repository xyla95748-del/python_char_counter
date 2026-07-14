#اولا حساب العمر بي السنه و الشعر وبعدها حسب كام يوم عشته بي كام شهر بي طام ساعه
print ("___Hello App____")
years = int(input("Enter your years: "))
month = int(input("Enter your month: "))
age = 2026 - years
month_1 = (7 - month)+ age*12
age =month_1 //12
month_1%=12
print("your age is : "+str(age) +" year and "+str(month_1)+" month\n")
age_Day = age*365
month_2 = age*12
hours = age_Day*24
print(f"your have lived for {age_Day} days  \n")
print(f"your have monthend for {month_2} month  \n")
print(f"your have hours for {hours} hours \n")

