#Collecting candidate's details.
print("UNILAG Admission Eligibility Checker for 2025/2026 Academic Session.")
print("Kindly fill the following appropriately to check your eligibily for admission.")
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
course = input("Enter your preferred course of study: ").title()
utme = int(input("Enter your UTME score: "))
waec = input("Do you have at least 5 credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics?: ").title()
postUTME = input("Did you paticipate in the UNILAG's online post UTME: ").title()
post_UTME_Score = int(input("Enter your POST UTME screening score result: "))
dept_cut_off = int(input("Enter your departmental cut-off mark (200-320): "))
student_details ={"Name" : name, "Age" : age, "Preferred Course of Study" : course, "UTME Score" : utme, "Do you have minimum of 5 credit pass": waec, "Did you participate in UNILAG's PUTME" : postUTME, "Your chosen department cut-off mark" : dept_cut_off}
# details = list(student_details)
# print(details)

eligibility = (age >= 16) and (utme >= 200) and (waec == "Yes") and (postUTME == "Yes") and (post_UTME_Score >= 200) and(dept_cut_off >= 200 <= 320)

if eligibility == True:
    print(f"Dear {name}, Congratulations! You are eligible for admission to UNILAG.")
elif eligibility == False:
    print(f"Dear {name}, Sorry, NYou are not eligible for admission")
else:
    print("Invalid entry. Kindly answer correctly.")

# result = {True: "Congratulations, you have been offered provisional admission", False: "Sorry, No admission given."}

# Final decision
# print(f"\nName: {name}\nAge: {age}\nCourse of study: {course}\nDuration: {duration}\nUTME score: {utme}\nIs UNILAG your first choice?: {choice}\nDo you  have 5 credit passes in your O' level result?: {waec}\nPOST UTME score: {post_utme}\nDepartmental Cut-off Mark: {dept_cut_off}\n\n\t====Admission Status===\nAdmission Status: Dear {name}, {result[eligibility]} to study {course} for {duration} years.")