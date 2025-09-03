#Dictionsry
# the syntax of dict is
# dictName = {key1: Value1, key2: value2}
# creating dict.
# #1 using {}
# student = {
#     "name": "Ada",
#     "age": 20,
#     "Course": "Computer Science"
# }
# print(student)

# #2 using the dict()
# student_info = dict(name="John", age = 25, course = "Maths")
# print(student_info)

# #empty dictionary
# student = {}
# print(student)
# # How to add  key-value pairs to an empty dictionary
# # Add key-value pairs to it
# student["name"] = "Goodness"
# student["Interest"] = "AI"
# student["Track"] = "AI_Dev"
# print(student)

# # #creating dict. of nos and their squares
# # squares = {x: x**2 for x in range(1,6) }
# # print(squares)

# # #with condition ie dict. of even numbers and their cubes
# # evensCube = {x:x**3 for x in range(1, 10) if x % 2 ==0}
# # print(evensCube)

#from existing dict.
# students = {"Ada": 85, "John": 40, "Musa": 65 }
# print(students) 
# #filter students who passed (score >= 50)
# passedStudents = {name: score for name, score in students.items() if score >= 50}
# print(passedStudents)

# # #using string keys
# # names = ["Ada", "John", "Musa"]
# # lengths = {name: len(name) for name in names}
# # print(lengths)

# #define a dict.
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# print(student)
# #using key
# print(student["name"])
# #using get() method
# print(student.get("age"))
# print(student.get("grade", "Not Found"))
# #Modifying Dict.: change value 
# student["age"] =21
# student["grade"] = "A"
# print(student)

# #removing items from dict.
# #using pop()
# student.pop("grade")
# print(student)

# #using popitem() to remove last inserted key-value
# student.popitem()
# print(student) 

# #using del keyword
# del student ["name"]
# print(student)

# #using clear () to remove all items
# student.clear()
# print(student)

# #Dict. methods
# #1 using .keys()
# person = {"name": "Emeka", "age":30}
# print(person.keys())
# #using .value()
# print(person.values())
# #using .items() every entry
# print(person.items())
# #using .update()
# person.update({"age": 31, "city": "Lagos"})
# print(person)

# #nested dictionaries
# students = {
#     "student1": {"name": "Ada", "age": 20},
#     "student2": {"name": "John", "age": 22}
# }
# print(students["student1"]["name"]) #to access nested data 

# #looping through dict.
# #Define a dict.
# student = {"name": "Ada", "age": 20, "course": "computer science"}
# #loop through keys; returns each on a new line
# for key in student:
#     print(key)

# #loop through values
# for value in student.values():
#     print(value)

# #loop through key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")

# #storing a students' biodata
# student = {
#     "name": "Chinedu",
#     "age": 19,
#     "department": "Engineering",
#     "subjects": ["Maths", "physics", "Chemistry"],
#     "is_full_time": True
# }
# print(f"name: {student["name"]}")
# print(f"subjects: {', '.join(student['subjects'])}")

# #storing details
# student = {"name": "Chinedu","age": 19, "department": "Engineering", "subjects": ["Maths", "Physics", "Chemistry"], "is_full_time": True}
# print(f"Name: {student["name"]}")
# print(f"subjects:{", ".join(student['subjects'])}")

# List of dictionaries - Each student has their own dictionary
# students = [
#     {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
#     {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
#     {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
# ]

# print(students[0]["Name"])   
# print(students[1]["Track"]) 

# # Dictionary of dictionaries - Each student is keyed by their ID
# students = {
#   "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
#   "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
#   "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
# }
# print(students["AI020"]["Name"])   
# print(students["AI030"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1])
