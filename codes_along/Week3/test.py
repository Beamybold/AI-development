# # Ask for the applicant's Basic Info
# name = input("Enter your name: ").upper()
# gender = input("Enter your gender: ").upper()


# # Ask student for University choice
# # Ask student to input number of WASSCE sitting
# # Ask student to enter subjects and the reults
# # Using TRY-EXCEPT-FINALLY for ValueErrors and TypeErrors 
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age >= 16:
#             try:
#                 utme_score = int(input("Enter your UTME score: "))
#                 if utme_score >= 200:
#                     try:
#                         print()
#                         uni_choice1 = input("Enter your University first choice: ").upper()
#                         uni_choice2 = input("Enter your University second choice: ").upper()
#                         uni_choice3 = input("Enter your University third choice: ").upper()
#                         if uni_choice1 == "UNILAG":
#                             o_level = input("Do you have an O'level result from one sitting ('Yes' or 'No'): ").lower()
#                             if o_level == "yes":
#                                 o_level_subjects = input("Enter five relevant subjects including Maths and English: ").split()
#                                 o_level_subjects1= input(f"Enter the result for English ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
#                                 o_level_subjects2= input(f"Enter the result for Maths: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
#                                 o_level_subjects3= input(f"Enter the result for {o_level_subjects[2]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
#                                 o_level_subjects4= input(f"Enter the result for {o_level_subjects[3]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
#                                 o_level_subjects5= input(f"Enter the result for {o_level_subjects[-1]}: ('A1', 'B2, 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9': ").upper()
#                                 o_level_results = ((o_level_subjects1) and (o_level_subjects2) and (o_level_subjects3) and (o_level_subjects4) and (o_level_subjects5))
#                                 if ((o_level_results == 'A1') or (o_level_results == 'B2') or (o_level_results == 'B3') or (o_level_results == 'C4') or (o_level_results == 'C5') or (o_level_results == 'C6')):
#                                     putme_exam = input("Did you participate for the Post UTME ('Yes' or 'No'): ")
#                                     if putme_exam == "yes":
#                                         putme_score = int(input(f"Enter your PUTME Score: "))
#                                         if ((putme_score >= 200) or (putme_score == 400
#                                                                      )):
#                                             print(f"Your post UTME score is {putme_score}")
#                                             print("Admission Granted")
#                                             break
#                     except TypeError:
#                         print("str and int not allowed")
#             except ValueError:
#                 print("Cannot convert str to int!")
#     except Exception as e:
#         print("Unexpected error:", e)
#     finally:
#         print("Traceback")



    

#     # Federal Government Scholarship 

# # Ask for the applicant's Basic Info
# name = input("Enter your name: ").upper()
# gender = input("Enter your gender: ").upper()


# # Checking for qualification
# # Using TRY-EXCEPT-FINALLY for ValueErrors and TypeErrors 
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if (age >= 16):
#             try:
#                 score = score = int(input("Enter your score: "))
#                 if (score >= 70):
#                     citizen = input("Are you from Nigeria? 'yes' or 'no': ")
#                     if (citizen == "yes"):
#                         Undergraduate_student = input("Are you a full time undergraduate student from a recognised Nigerian university? Yes or No:")
#                         if (Undergraduate_student == "yes"):
#                             other_student_scho = input("Do you have a scholarship from any Oil and Gas Industry (local or international)? Yes or No: ")
#                             if (other_student_scho == "no"):
#                                 academic_subjects = input("Enter five subjects including Maths and English: ").split()
#                                 academic_result1= input(f"Enter the result for {academic_subjects[0]}: ").upper()
#                                 academic_result2= input(f"Enter the result for {academic_subjects[1]}: ").upper()
#                                 academic_result3= input(f"Enter the result for {academic_subjects[2]}: ").upper()
#                                 academic_result4= input(f"Enter the result for {academic_subjects[3]}: ").upper()
#                                 academic_result5= input(f"Enter the result for {academic_subjects[-1]}: ").upper()
#                                 results = ((academic_result1) and (academic_result2) and (academic_result3) and (academic_result4) and (academic_result5))
#                                 if ((results == 'A1') or (results == 'B2') or (results == 'B3')):
#                                     print(f"{name}, You are eligible for Scholarship!.")
#                                     break
#                                 else:
#                                     print(f"{name}, You do not possess the required grade. Not eligible!")
#                                     break
#                             else:
#                                 print(f"{name}, You cannot apply for another scholarship!")
#                                 break
#                         else:
#                             print(f"{name}, Only full time students are eligible!.")
#                             break
#                     else:
#                         print(f"{name}, You are not eligible! You must be a citizen to qualify.")
#                         break
#                 else:
#                     print("You do not meet the score requirement")
#                     break
#             except TypeError:
#                 print("str and int are not allowed")
#                 break
#     except ValueError:
#         print("Cannot convert int to str")
#     finally:
#         print("Traceback")



# student_file = {
#      "Basic Info": {
#         "Name": name,
#          "Age": age,
#          "Gender": gender,
#          "Nationality": citizen
#      },
#      "Academic Info": {
#          "Score": score,
#          "Enrollment": Undergraduate_student,
#          "Other Scholarships": other_student_scho,
#          "Subjects": academic_subjects,
#          "Results": results
#      },
# }


# # Output
# print("\n-----------------STUDENT FILE----------------------")
# print(f"Name:\t\t\t{student_file['Basic Info']['Name']}")
# print(f"Age:\t\t\t{student_file['Basic Info']['Age']}")
# print(f"Gender:\t\t\t{student_file['Basic Info']['Gender']}")
# print(f"Nationality:\t\t{student_file['Basic Info']['Nationality']}")
# print("\n-------------------ACADEMIC INFO--------------------")
# print(f"Score:\t\t\t{student_file['Academic Info']['Score']}")
# print(f"Enrollment:\t\t{student_file['Academic Info']['Enrollment']}")
# print(f"Other Scholarships:\t{student_file['Academic Info']['Other Scholarships']}")
# print(f"Subjects:\t\t{student_file['Academic Info']['Subjects']}")
# print(f"Results:\t\t{student_file['Academic Info']['Results']}")





# This is a simulated USSD menu interaction for a mobile clinic. 
# The products aim is to make maternal healthcare accessible to expectant mothers in rural areas without smartphones. 
# The end goal is to reduce maternal mortality rate in underserved regions in Nigeria.
# Grant users access to medical personnels. 
# No doubt there are a lot of infrastructure, that the govt needs to put in place but this simply a logic.
# Please use the prescribed prompts commented on each block.
# I have used break to stop the inputs that aren't prescribed. 
# I really enjoyed this....To be continued. #KanyisolaTheIncomingTechSisInshaAllah

# # Using TRY-EXCEPT for IndexErrors and TRY-EXCEPT-FINALLY
# print("=============================================================")
# print("Q12: SIMULATED USSD MENU INTERACTION")
# print("=============================================================")
# # Ask user to input USSD
# while True:
#     ussd = str(input("Enter the USSD code:\n"))
#     if ussd == "*882#":
#         print("\nFor English, Press 1")
#         print("Fun ede Yoruba, te eji")
#         print("Maka asusu Igbo, pia ato")
#         print("Domin Hausa, danna hudu")
#         print("For Pidgin, press faif\n")
#         lang_option = str(input("Please enter an option: ")) # Please enter 1, I'm still a learner...LOL
#         if lang_option == "1":
#             print("\nWelcome to NCC Mobile Clinic, How can we be of service to you today?:\n ")
#             print("Press 1, For emergency")
#             print("Press_2, For the nearest PHC")
#             print("press_3, To speak with a physician")
#             print("Press 00, Next")
#             option = input("\nPlease select an option:")
#             if option == "1":
#                 emergency = input("What's your emergency?: ")
#                 break
#             elif option == "2":
#                 location = input("Enter your location: ")
#                 break
#             elif option == "3":     # Please enter 3 for now.
#                 name = input("\nPlease enter your name: ").upper()
#                 nhis_no = (input("\nPlease enter your NHIS card no: "))
#                 if nhis_no.isdigit():
#                     print(f"\nWelcome {name}, NHIS No: {nhis_no}".strip())
#                 else:
#                     print("Invalid input. Please enter a number.")
#                     break
#                 print("\nPress 1, to speak with the Matron")
#                 print("Press 2, to speak with the Gynaecologist")
#                 print("Press 3, to speak with the General practitioner\n")
#                 physician_option = (input("\nWho you would like to speak with:")) # please enter 2
#                 if physician_option == "1":
#                     print(f"\n{name, nhis_no}, Please stay on the line while i connect you to the Matron")
#                     break
#                 elif physician_option == "2":
#                      print(f"\n{name, nhis_no}, Please stay on the line while i connect you to the Gynaecologist")
#                      print(f"\nThank you for choosing our services, your call with the gynaecologist lasted for 2hrs")
#                      Matron_per_hour = 200
#                      Gynaecologist_per_hour = 800
#                      General_practitioner_per_hour = 300
#                      Gynaecologist_per_hour *= 2
#                      print(f"\nYour bill is:", Gynaecologist_per_hour)
#                      nhis_wallet = 1500
# # Using TRY-EXCEPT for IndexErrors and TRY-EXCEPT-FINALLY
#                 try:
#                         if nhis_wallet <= Gynaecologist_per_hour:
#                             raise ValueError ("Insufficient balance, please credit your wallet!")
#                         nhis_wallet -= Gynaecologist_per_hour
#                         print(f"\nTransaction successful, NHIS wallet balance is: {nhis_wallet}") 
#                         print("Thank you for using our product.")
#                 except ValueError as e:
#                         print("Error message:", e)
#                 except Exception as e:
#                         print("Service Error", e)
#                 finally:
#                         print("Session Closed!")
#                         print(f"\n{name, nhis_no}, Please stay on the line while i connect you to the Gynaecologist")
#                         print(f"\nThank you for choosing our services, your call with the gynaecologist lasted for 1hr 45 mins.")
#                         Matron_per_hour = 200
#                         Gynaecologist_per_hour = 400
#                         General_practitioner_per_hour = 300
#                         Gynaecologist_per_hour *= 1.75
#                         print(f"\nYour bill is:", Gynaecologist_per_hour)
#                         nhis_wallet = 1500
#                         if nhis_wallet >= Gynaecologist_per_hour:
#                          nhis_wallet -= Gynaecologist_per_hour
#                         print(f"\nTransaction successful, NHIS wallet balance is: {nhis_wallet}") 
#                         print("Thank you for using our product.")
#                         break
#             else:
#                 print("\nInsufficient fund, Please credit your NHIS wallet")
#                 break
#         else physician_option == "3":
#                     print(f"{name, nhis_no}, Please stay on the line while i connect you to the General Practitioner")
#                     break
#     else: 
#                     print("You have not selected an option.")
#                     break
#     elif option == "00":zz
#                 print("Press # to go back to the main menu.")
# else:
#                 print("You have not selected an option.")
#                 break
#         elif lang_option == "2":
#             print("E kaa bo si ile-iwosan NCC, bawo ni a se le ranyi lowo loni?: ")
#             break
#         elif lang_option == "3":
#             print("Nnoo, i nabata NCC Clinic, kedu ka anyi nwere ike isi nyere gi aka taa?: ")
#             break
#         elif lang_option == "4":
#             print("Barka da zuwa Asibitin NCC, ta yaya za mu iya taimaka muku a yau?: ")
#             break
#         elif lang_option == "5":
#             print("Welcome to NCC Clinic, How we fit take help you today?: ")
#             break
#         else:
#             print("Invalid option. Please enter correct option.")
#             break
#     else:
#         print("Invalid USSD!")
#         break


    
# Using TRY-EXCEPT for IndexErrors and TRY-EXCEPT-FINALLY
# Create a dictionary called store
store = {'candles': 30, 'bottle of fruit wine': 150, 'birthday cards': 150, 'boxes of tea': 18}
items = store.keys()
items_qty = store.values()

try:
    print(store["beans"])
except KeyError:
    print("\nOut of index range\n")

while True:
    print(store)
    order = input(f"\nWe currenlty have various items for sale, please enter your order: ").lower()
    if order in items:
        print(f"\n{order} are available")
        quantity= int(input("\nPlease enter the quantity: "))
        order_update = store.copy()
        print(order_update)
        try:
            if quantity > order_update[order]:
                raise ValueError("\nQuantity not available")
            order_update[order] -= quantity
        except ValueError as e:
            print("\nError message:", e)
        except Exception as e:
            print("\nError message:", e)
        finally:
            print("\nSession closed.")





# # To run each error code... comment the other code out first

# # Using TRY-EXCEPT for NameErrors
# user_names = []
# user1 = input("Please enter your name:")
# user2 = input("Please enter your name:")
# user3 = input("Please enter your name:")

# # Comment out to see the error message
# # try: 
# #     print(user11)
# # except NameError:
# #     print("users1 not defined")

# # Create an empty list and ask users for their numbers
# user_nums = []
# user_num1 = (input("Please enter your phone number:"))
# user_num2 = (input("Please enter your phone number:"))
# user_num3 = (input("Please enter your phone number:"))

# # Add user numbers to the empty list
# user_nums.append(user_num1)
# user_nums.append(user_num2)
# user_nums.append(user_num3)

# # Convert list of user numbers to tuple
# user_nums_tuple = tuple(user_nums)
# print(user_nums_tuple)

# # Using TRY-EXCEPT for TypeErrors
# try:
#     print(user_nums_tuple = "ABC" + 12345)
# except TypeError:
#     print("str and int not allowed")






#     # Add user input
# member1 = input("Please enter your name:").split(",")
# member2 = input("Please enter your name:").split(",")
# member3 = input("Please enter your name:").split(",")


# #Convert the names of the member to set
# member1_set = set(member1)
# member2_set = set(member2)
# member3_set = set(member3)
# print(set.union(member1_set,member2_set,member3_set)) #print("Here are the names:", ",".split(names_list))


# # Create a dictionary where each name is key and value is length
# unique_member1 = {name: len(name) for name in member1_set}
# unique_member2 = {name: len(name) for name in member2_set}
# unique_member3 = {name: len(name) for name in member3_set}


# ## Using TRY-EXCEPT for KeyError and IndexError
# try:
#     print(unique_member1["gender"])
# except KeyError:
#     print("Key not found")


# unique_members = (unique_member1, unique_member2, unique_member3)
# try:
#     unique_members[3]
# except IndexError:
#     print("Index out of range")





# # Ask user to enter a word

# word = input("Please enter the longest word you know: ")

# try:
#     word = int("Hippotamus")
# except ValueError:
#     print("Cannot convert str to int")
# finally:
#     print("Traceback")
    

# # # Define the vowels 
# # vowels = 'a','e','i','o','u','A','E','I','O','U'
# # vs = sum(1 for char in word if char in vowels)
# # print(f"There are {vs} vowel(s) in the word")
