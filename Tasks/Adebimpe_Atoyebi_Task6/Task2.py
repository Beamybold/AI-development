#Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
Attendant = "Tayo", "Yul", "Vic", "Temz", "Jone", "Kim", "Mac"
seminarAttendan = set(Attendant)
seminarAttendant = sorted(seminarAttendan)
print(f"{seminarAttendant}")
