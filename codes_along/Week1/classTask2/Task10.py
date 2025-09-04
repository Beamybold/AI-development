schoolName = input("Enter your school name: ")
tuitionFee = float(input("Enter your tuition fee: "))
housingFee = float(input("Enter your housing fee: "))
feedingFee = float(input("Enter your feeding fee: "))
total = tuitionFee + housingFee + feedingFee
print(f"\t{schoolName}\n\t\tRECEIPT\n\tTuition Fee\t{tuitionFee}\n\tHousing fee\t{housingFee}\n\t Feeding Fee\t{feedingFee}")
print(f"\t\tTOTAL\t{total}")