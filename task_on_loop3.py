student = {
"name": "legolas",
"has_registered": True,
"has_paid": True,
"has_internet": False
}


if student["has_registered"]:
    if student["has_paid"]:
        if student["has_internet"]:
            print("Allow Access")
        else:
            print("Check your connection")
    else:
        print("Pay your fees")
else:
    print("Access Denied")
