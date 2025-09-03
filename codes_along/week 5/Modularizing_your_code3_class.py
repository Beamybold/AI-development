# class Student: # creating a class for student
#     def __init__(self, name, course, level): 
#         print("Creating a new a student....")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created")

# kemi = Student("Kemi Adebayo", "Computer Science", 300)
# print(kemi.course)
        

# #init and self working together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating Student object.....")
#         self.name = name # Step 2: Assign name to THIS object
#         self.state__of_origin = state   # Step 3: Assign state to THIS object
#         self.course = course   # Step 4: Assign course to THIS object
#         self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
#         print(f"Step 6 {self.name} from {self.state__of_origin} is ready!")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"

# ayo = NigerianStudent("Ayo Salako", "Osun", "medicine and Surgery")
# print(ayo.name)
# print(ayo.student_id)




# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} article")
      

    # def buy_airtime(self, amount):
    #     self.airtime += amount #self ensures it goes to he right person
    #     return f"{self.name} now has ₦{self.airtime} airtime"

 
# Ola = PhoneUser("Ola Oke", "MTN")
# ike = PhoneUser("Ike Kolapo", "Glo")

# #Each person's actions affect only their own account
# print(Ola.buy_airtime(500))
# print(ike.buy_airtime(1000))
# print(ike.airtime)
# print(Ola.airtime)



#Defing attribute of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

    def get_cgpa(self, aggregate):
        self.cgpa += aggregate
        return f"{self.cgpa} is {self.name} CGPA"
    

#Creating a student object
Ope = Student("Ope Bello", "Computer Science", 400, "Oyo")

#Accesssing attributes
print(Ope.name)
print(Ope.course)
print(Ope. get_cgpa(4.91))

#Types of attributes 
#1-Instance Attribute: unique to each object

student1 = Student("Ayo Musa", "SLT", 100, "Lagos")
student2 = Student("Ife Oye", "Mathematics", 400, "ogun")

print(student2.name)

#2- class attribute: shared by all object of the class
class Student: 
    university = "OAU"
    
    def __init__(self, name, course):
        self.name = name 
        self.course = course
    def pay_school_fees(self):
        return f"{self.name} has paid school fees"  
student1 = Student("Ayo Musa", "SLT")
student2 = Student("Ife Oye", "Mathematics") 

        
print(student1.name)
print(student1.university)


#Methods: They are functions that belong to a class. They describes that actions an objects can perform not what they look like eg things a student can do eg study(), writeExam( etc)
class Student:
    def __init__(self, name, course, level):
        #Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

#Method: actions the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fes for {self.level}level"
    
#Method- Another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered for {self.course}"
        else:
            return f"{self.name} must pay school fee first to register"
        
#Another method
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        else:
            return f"No grades provided!"

#Using methods
Folarin = Student("Folarin Oke", "Music", 300)
print(Folarin.pay_school_fees())
print(Folarin.register_courses())
print(Folarin.calculate_cgpa({4.5, 4.9, 5.0}))

#Types of methods: 
#1 - Instance methods - works with specific student
university = "OAU"
    
def __init__(self, name, course):
    self.name = name 
    self.course = course
def pay_school_fees(self):
        return f"{self.name} has paid school fees"  
student1 = Student("Ayo Musa", "SLT")
student2 = Student("Ife Oye", "Mathematics")
def pay_school_fees(self):
    return f"{self.name} has paid school fees" #copy to the class function where universty was defined

#2 - class methods - work with class-level data
@classmethod
def get_univeraity(cls):
    return cls.university

#3 - Static methods: This does not need object or class data
@staticmethod
def academic_calendar():
    return "Academic session runs from September to July"

#Relationship between  attributes and methods
    #-Atttributes store the data while methods use and modify the data.

class Bank