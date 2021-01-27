print("WELCOME TO LOVE CALCULATOR")
his_name = input("Enter his name: \n").lower()
her_name = input("Enter her name: \n").lower()

t1 = his_name.count("t")
r1 = his_name.count("r")
u1 = his_name.count("u")
e1 = his_name.count("e")

t2 = her_name.count("t")
r2 = her_name.count("r")
u2 = her_name.count("u")
e2 = her_name.count("e")

true_total = t1 + t2 + r1 +r2 + u1 + u2 + e1 + e2

l1 = his_name.count("l")
o1 = his_name.count("o")
v1 = his_name.count("v")
e1 = his_name.count("e")

l2 = her_name.count("l")
o2 = her_name.count("o")
v2 = her_name.count("v")
e2 = her_name.count("e")

love_total = l1 + l2 + o1 + o2 + v1 + v2 + e1 + e2

love_score = (f"{true_total}{love_total}")
print(love_score)
