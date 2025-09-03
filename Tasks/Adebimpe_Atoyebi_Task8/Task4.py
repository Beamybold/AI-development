student = {}
name = input("enter your name: ").title()
age = int(input("enter your age: "))
scores = [70, 85, 90, 64, 82]
averageScore = sum(scores)/len(scores)
passed = averageScore >= 75
Teenager = age >= 13 and age <= 19
student = {"Name" : name, "Age" : age, "scores" : scores, "Passed" : True, "Teenager" : True}
StudentDetails = list(student)
print(f"Student Records: \nName: {name}\nAge: {age}\nScores: {scores}\nPassed: {passed}\nTeenager: {Teenager}")

# print(averageScore)

