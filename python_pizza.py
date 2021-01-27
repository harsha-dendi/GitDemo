print("welome to python pizza")

size = input("what size pizza you ordering, type S for small, M for medium or L for large\n")
pepporoni = input("Would you like to add pepporoni, type 'Y' for yes or 'N' for no\n")
cheese = input("would you like to add cheese, type 'Y' for yes or 'N' for no\n")

bill = 0

if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25

if pepporoni == "Y":
    if size =="S":
        bill += 2
    if size == "M":
        bill += 3
    if size == "L":
        bill += 3
if cheese == "Y":
    bill += 1

print(f"your final bill is: {bill}")
