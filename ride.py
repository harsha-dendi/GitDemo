height=int(input("what is your height in cm?"))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster")


    age = int(input("what is your age?"))
    if age < 12:

        bill = 5

        print(f"your bill is £{bill}")

    elif age <= 18:
        bill = 7
        print(f"your bill is £{bill}")
    else:
        bill = 12
        print(f"your bill is £{bill}")
    want_photo=input("Do you want the photo: say yes or no? ")
    if want_photo == "yes":
       bill += 3
    print(f"your bill is £{bill}")
