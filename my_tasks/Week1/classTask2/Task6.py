customerName = input("Enter your name: ")
unitConsumedInKwh = int(input("Enter unit consumed: "))
costPerUnit = float(input("Enter cost per unit: "))
Total = unitConsumedInKwh * costPerUnit
print(f"\tELECTRICITY BIll\n{customerName}\nReceipt\n.................\nUnit consumed in KW/H\t{unitConsumedInKwh}\nCost per unit\t{costPerUnit}\nTotal\t{Total}")