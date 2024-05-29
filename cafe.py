#Cafe management system
print("*****Hello*****")
#greet the person
a = "welcome to cafe maya"
print(a.capitalize())
print("Below is our menu,Please select your order")
dict1 = {"tea": 25, "milkshake": 40, "ice cream": 45, "Shawarma": 120}

#print menue
print(" tea:25\n milkshake:40\n ice cream:45\n shawarma :120\n")

order1 = input(("Please enter your order:"))

quantity1 = int(input(("Please enter the quantity:")))

total = 0
if order1 in dict1:
  total = +dict1[order1] * quantity1
  print("Your {} is on the way".format(order1))
  print("Your total bill is {}".format(total))
else:
  print("Sorry,we dont have this {} item ".format(order1))

#second time the person if he or she wants to order anything else
choice = int(
    input("Would you like to order anything else? Enter 1 for yes, 0 for no:"))

if (choice == 1):
  order2 = input("enter your next order:")
  quantity2 = int(input("enter the quantity:"))
  if order2 in dict1:
    total_new = total + dict1[
        order2] * quantity2  # update the final bill in total_new variable
    print("Your {} is on the way".format(order2))
    print("Your total bill is {}".format(total_new))
else:
  print("Thank you for visiting")
