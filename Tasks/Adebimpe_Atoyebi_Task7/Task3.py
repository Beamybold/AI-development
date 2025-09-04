days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday")
activities = []
for day in days:
    activity = input(f"what activities do you have cary out on {day}: ")
    activities.append(activity)
    daysAndactivities = {day:activity for day, activity in zip (days, activities)}
    print(f"{day}:{activity}")
    