score = int(input("Enter the score of the student: "))

if score >= 70 and score <= 100:
    print("The grade is A")
elif score >= 50 and score <= 69.9:
    print("The grade is B")
elif score >= 40 and score <= 49.9:
    print("The grade is C")
elif score >= 30 and score <= 49.9:
    print("The grade is D")
elif score >= 0 and score <= 30:
    print("The grade is F")
else:
    print("This is an invalid range")
