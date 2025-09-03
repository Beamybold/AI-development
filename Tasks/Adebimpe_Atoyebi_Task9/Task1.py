"""12. Simulated USSD Menu Interaction
 - You are to design a mock USSD interface for a mobile service.
 - Requirements:
   1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
   2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
   3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
   4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
   5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
   6. Ask for an amount (if applicable) and store it as a number using type casting.
   7. Display a final message summarizing the transaction.
"""


ussdCode = "*123#"
print("Welcome to MTN self-service center")
ussd = input(f"dial {ussdCode}: ")
CheckBalance = "1"
BuyAirtime = "2"
BuyData = "3"
shareData = "4"



while True:
    if ussd == ussdCode:
        print("Choose an option")
    else:
        print(f"Incorrect entry. dial {ussdCode}")
        break
    print("MENU\n1. Check Balance\n2. Buy Airtime\n3. Buy Data\n4. Share Data\nChoose an option.")
    balance = 3300
    Data_Bal = 5000
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your balance is N{balance}")
    elif choice == "2":
        amount = int(input("Enter the amount of airtime you want to buy: "))
        balance += amount
        print(f"Your total airtime balance is N{balance}")
    elif choice == "3":
        amount = int(input("Enter the amount of airtime you want to buy: "))
        Data_Bal += amount
        print(f"Your data purchase was successful. Your new data balance is {Data_Bal}MB")
    elif choice == "4":
        amount = int(input("Enter the amount of data you want to share: "))
        if amount <= Data_Bal:
            Data_Bal -= amount
            print(f"You have share {amount}.\nYour data balance emains {Data_Bal}MB")
        else: 
            print("Insufficient data balance. Buy data and try again.")
        break
    else:
        print("Invalid option. Input the right number")




      
