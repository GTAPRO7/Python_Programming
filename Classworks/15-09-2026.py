##Dictionary

Student = {
	"name": "Gokul",
	"reg_no": 2647224,
	"age": 24,
	"class": "2 MCA B"
}

print(Student)
print(Student["name"])
print(Student.get("name"))
##print(Student["mark"]) KeyError: 'mark'
print(Student.get("mark"))

##Adding a New Key-Pair Value
print("\nAdding..........")
Student["marks"] = 95
print(Student)

##Updating an existing value
print("\nUpdating..........")
Student.update({
	"age": 23,
	"marks": 97

})
print(Student)

print("\nPrinting using for loop..........")
for key, value in Student.items():
	print(key, ":", value)

print("\nCopy..........")
copy = Student.copy()
print(copy)

print("\nRemove..........")
##print("Removing age :",Student.pop()) TypeError: pop expected at least 1 argument, got 0
print("Removing age :",Student.pop("age"))
print("Popeditem :",Student.popitem())

print("\nClear..........")
print("Clear :", Student.clear())

print("\nDictionary Comprehension..........")
numbers = [1,2,3,4,5,6,7]
print(numbers)
squares = {n: n*n for n in numbers}
print(squares)

print("\nPrinting only even numbers..........")
even = {n: n*n for n in numbers if n % 2 == 0}
print(even)

print("\nConditional Dictionary Comprehension(using range)..........")
num1 = range(1, 11)
print(num1)
even = {n: n*n for n in num1 if n % 2 == 0}
print(even)

print("\nNested Dictionary..........")
Student1 = {"2647224": {
			"name": "Gokul",
			"marks": {"Python": 90,
		  		  "DSA": 85,
		  		  "OS": 95,
				 }
			},
	   "2647263": {
			"name": "Hari",
			"marks": {"Python": 95,
		  		  "DSA": 90,
		  		  "OS": 97,
				 }
			}	
	  }

print(Student1)

##Access Hari's DSA Marks
print("\nPrinting Hari's DSA Marks..........")
print(Student1["2647263"]["marks"]["DSA"])
print("\nPrinting Gokul's Python Marks..........")
print(Student1["2647224"]["marks"]["Python"])

print("\nPrinting Hari's Average Marks..........")
marks = Student1["2647263"]["marks"]
avg = sum(marks.values()) / len(marks)
print("Average :", avg)

##Functions
print("\nTemperature convertion using function..........")

def c_to_f(cel):
	return (cel * 9 / 5) + 32

def f_to_c(fht):
	return (fht - 32) * 5 / 9

cel = int(input("Please eneter the celsius :"))
print("Celsius to Fahrenheit",c_to_f(cel))

fht = int(input("Please eneter the fahrenheit :"))
print("Fahrenheit to Celsius",f_to_c(fht))


print("\nStudent Marks Analyzer..........")
def analyze_marks(marks):
	total = sum(marks)
	average = total/len(marks)
	highest = max(marks)
	lowest = min(marks)

	return total, average, highest, lowest

marks = [85, 98, 80, 75, 90]

total, average, highest, lowest = analyze_marks(marks)

print("Total :",total)
print("Average :",average)
print("Highest :",highest)
print("Lowest :",lowest)

print("\nPassword Verification (8 cahr and atleast 1 digit)..........")

def val_paswd(paswd):
	if len(paswd) < 8:
		return False

	for character in paswd:
		if character.isdigit():
			return True
	return False

paswd = input("Please eneter the password :")

if val_paswd(paswd):
	print("Valid Password")
else:
	print("Invalid Password")


print("\nStudent Attendance - Function to calculate att %..........")

attendance = {
	"Anu": [1,1,0,1,1],
	"Ravi": [1,0,1,1,0],
	"John": [1,1,1,1,1]
}
	








