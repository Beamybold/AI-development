# collect stuents biodata
name = input("enter your name: ").title()
age = int(input("Enter your age: "))
gender = input("Enter your gender: ").title()
courses = input("enter your courses: ").split()
courseLst = [courses]
studentDetails = {
    "Name": name,
    "age": age,
    "Courses": courses
}
print(studentDetails)
print(f"Name\t{name}\nAge\t{age}\nGender\t{gender}\nCourses\t{courses}")