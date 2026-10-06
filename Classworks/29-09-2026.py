#Exceptions
print("Error Handling..........")
print()

while True:
	try:
	    310 * (1 / 10)
	    4 + prod * 3 
	    '5' + 5
	    break
	except (RuntimeError, TypeError, NameError, ZeroDivisionError):
		print("Error brooo.........")
		break

def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("Division bt Zero!")
	except TypeError:		
		print("Type Error")
	else:
		print("Result is: ",result)
	finally:
		print("Excecuting finally clause")

divide(2,1)
divide(2,0)
divide("2","1")

#re Module
print("\nRe Module..........")
print()


import re
txt = "Welcome he to The re module Christite"

search1 = re.search("he", txt)
print(search1)
print(search1.span())
print(search1.string)
print(search1.group())

fall1 = re.findall("he",txt)
print(fall1)
split1 = re.split("he",txt)
print(split1)
sub1 = re.sub("he","5",txt)
print(sub1)


print("\nRe Module 2..........")
print()

txt = "Welcome to The re module moddule or cocept 29 Sep 2026 module moodle"
search1 = re.findall("[odu]", txt)

search2 = re.findall("\\d", txt)

search3 = re.findall("We..ome", txt)

search4 = re.findall("^Wel", txt)

search5 = re.findall("26$", txt)

search6 = re.findall("mo.*p", txt)

search7 = re.findall("mo.?ule", txt)

search8 = re.findall("mo.{3}e", txt)

search9 = re.findall("module|concept", txt)

search10 = re.findall("mo(du|od)le", txt)

search11 = re.findall(r"mo(?:du|od)le", txt)

search12 = re.findall("r'mo*e$'", txt)

search13 = re.findall(r"mo*e$", txt)

search14 = re.findall("[a-zA-Z]", txt)

print(search1)
print(search2)
print(search3)
print(search4)
print(search5)
print(search6)
print(search7)
print(search8)
print(search9)
print(search10)
print(search11)
print(search12)
print(search13)
print(search14)


#Password Validation - Password should contain at least 8 characters, 1 uppercase, 1 lowercase and 1 digit

def paswd_valid():
	paswd = input("Please enter the password")
	
	val = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[0-9]).{8,}$)"

	if re.match(val, paswd):
		print("Valid Password")
	else:
		print("Invalid Password")

paswd_valid()


	