# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
"""This is a program to check the eligibility of a candidate with criterias stated to be the person age must be less than 18 and have a score greater than 70. In the above candidate entry, the eligibility is false becacause non of the criteria was met
"""

# name = input("Enter your name: ")
citizenship = input("Enter your country of citizen: ")
Enrollment = input("Are you a student of a recognised Nigerian university? ")
otherScholarships = input("Are you a beneficiary of any other oil and gas organization? ")
academicQualification = input("Do you have 5 As and Bs in your O'level including English and maths? ")
eligibility = ((citizenship == "Nigeria") or (citizenship == "Nigerian")) and (Enrollment == "Yes") and (otherScholarships == "No") and (academicQualification == "Yes")
print(f"Country of citizenship: {citizenship.title()}\nAre you a student of a recognised university: {Enrollment.title()}\nAre you a beneficiary of any Oil and Gas industry scholarship: {otherScholarships.title()}\nDo you have 5 As and Bs in your O'level including English and maths: {academicQualification.title()}\nEligible: {eligibility}")

###name: Ayo Ade
# Country of citizen: Nigeria
# Student of a recognised Nigerian university: Yes
# Beneficiary of any other oil and gas organization: No
# Have 5 As and Bs in your O'level including English and maths: Yes
