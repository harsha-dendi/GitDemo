print("Welcome to the tip calculator")
bill = float(input("what was your total bill?\n"))
tip = float(input("what percentage tip would you like to give? 10, 12 or 15?\n"))

People = float(input("How many people to split the bill?\n"))

Total_with_tip = (bill + (bill *(tip/100))

Bill_per_individual = (Total_with_tip / People)

print(f"Each person to pay:£{Bill_per_person})