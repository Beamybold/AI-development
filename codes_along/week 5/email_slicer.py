# @title 13. Email Slicer(Extract Username from Email)

"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""


# Email slicer app
while True:
    email = input("Enter your email address here: ")
    if "@" and ".com" in email and email.endswith(".com"):
        print("The email is validated")
    else:
        print("This input is not a valid email.\nFollow this format 'example@email.com'")
        continue

    stripper = email.split("@")
    print(email)

    print(stripper)
    try:
        username = stripper[0]
        domain = stripper[1]
        print(f"Your username is {username} and the domain is {domain}")
        break
    except Exception as e:
        print(f"The error was {e}")
        continue