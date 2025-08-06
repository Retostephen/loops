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

password = input("Enter your password: ")
confirm_password = input("Please confirm your password: ")

if password == confirm_password:
	print("Accepted")
else:
	print("Passwords Doesn't Match")













