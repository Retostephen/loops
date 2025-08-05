budget = float(input("Enter your budget: "))

if budget >= 1000:
    print("Google Pixel 9pro")
elif budget >= 500:
    print("Iphone")
elif budget >= 200:i
    print("Redmi")
else:
    print("Save More")
'''
if budget >= 1000:
    print("Google Pixel 9pro")
elif budget >= 200 and budget < 500:
    print("Redmi")
elif budget >= 500 and budget < 1000:
    print("Iphone")
else:
    print("Save More")
'''
'''
print("Iphone") if budget <= 500 and budget >= 1000 else print("Google Pixel 9pro")
print("Redmi") if budget <500 and budget <= 200 else print("Save More")

'''
