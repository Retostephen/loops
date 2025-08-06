'''
name = "Bankat"
name2 = "Hello" + " " + name

print(name)
print(name2)

add = -3 // 2
print(add)
'''


'''
countries = {
"Nigeria": "Abuja",
"Ghana": "Accra",
"Singapore": "Singapore"
	}


countries.update({"USA": "DC"})
print(countries)
countries = str(countries)
keys_list = list(countries.keys(countries))
print(keys_list)
print(type(countries))

keys_list = {*countries}
print(keys_list)
print(type(keys_list))
'''
'''
a = {"name": 1, "name2": 2}
b = {"class1": 3, "class": 4}
c = {"class": b}
a.update(b)
print(a)
print(c)
'''
'''
tanko = {"name": "tanko"}
core = {"name": "core"}

tanko.update(core)
#core.update(tanko)

print(tanko)
'''

#password = input("Enter your password: ")
#confirm_password = input("Please confirm your password: ")
'''
if password == confirm_password:
	print("Accepted")
else:
	print("Passwords Doesn't Match")
'''

users = ["core", "tk", "mp"]
user_name = input("Please enter your username: ")
is_verified = True

if user_name in users:
	print("User Exist")

	password = input("Enter your password: ")
	confirm_password = input("Please confirm your password: ")

	if password == confirm_password:
		print("Accepted")
	else:
		print("Passwords Doesn't Match")
	if is_verified:
		print("Verified User")
else:
	print("User doesn't exist")



'''
userDetails = {
username
balance
password
is_verified
	}
'''
#verification amount = (my choice)
#prompt login or register(check for valid input)
#if login is chosen: ask for username and password (check if username exist and if password matches)
#if register is chosen: ask for username (check if username doesn't exist and proceed to next step) and password and also balance. by default, is_verified = False. if asked to be verified and option selected yes (balance should be checked and if it's not upto the verification amount, print, insufficient amount, else deduct from balance and mark verified. If the user doesn't want to be verified, skip to login)
#after succesful registeration, prompt user to login




