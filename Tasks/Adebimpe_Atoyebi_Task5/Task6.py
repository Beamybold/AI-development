week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
# print(week)
# person = ("John", 25, "Nigeria")
# name, age, country = person
# print(Months)
print("Kindly enter your details")
name = input("enter your name: ").title()
gender = input("enter your gender: ").title()
courseTrack = input("Enter your couse track: ")
currentMonthNumber = int(input(f"enter your current month no{Months}: "))
currentDayNumber = int(input(f"enter your current day number{week}: "))
print(f"Name: \t\t{name}\nGender:\t\t{gender}\nCurrent Month\t({Months[currentMonthNumber -1]}\nCurrent Day\t{week[currentDayNumber -1]}")














