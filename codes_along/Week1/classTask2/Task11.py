Amount = float(input("Enter the amount in Naira: "))
exchangeRateDollar = float(input("Enter exchange to Dollars: "))
exchangeRatePounds = float(input("Enter the exchange rate in British Pound: "))
total = Amount * exchangeRateDollar
total1 = Amount * exchangeRatePounds
print("CURRENCY CONVERTER")
print(f"Naira\t#{Amount:,}\nDollar Rate\t${exchangeRateDollar:,}\nTOTAL\t#{total:,}")
print(f"Naira\#{Amount:,}\nPound Rate\t£{exchangeRatePounds:,}\nTOTAL\t#{total1:,}")