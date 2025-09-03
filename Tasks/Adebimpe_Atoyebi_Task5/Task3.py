# states = ("Edo", "Kwara", "Osun", "Lagos", "Ogun")
# print(states[0], states[4])
# print("Lagos" in states)
# print(len(states))

statelst = []
for i in range(5):
    states = input(f"Enter the states {i + 1}: ").title()
    statelst.append(states)
    states = tuple(statelst)
    print(f"{states[0]} and {states[-1]}")
    print("Lagos" in states)
    print(len(states))