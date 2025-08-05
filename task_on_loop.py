age = int(input("Enter your age: "))

if age >= 18:
    print("Can buy ticket")
    if age >= 60:
        print("Senior Discount")
elif age < 18 and age >= 12:
    print("Teen Ticket")
else:
    print("Kids Ticket")
