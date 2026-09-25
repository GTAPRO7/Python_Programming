#Encapsulation

print("\nDefault Arguments........")
print()

class Patient:

	def register(self, name, age = 0, disease = "Not specified"):
		print("Name: ",name)
		print("Age: ",age)
		print("Disease: ",disease)

p = Patient()

p.register("Anu")
print()
p.register("Anu", 30, "Diabetes")

print("\n*details........")
print()

class Patient:

	def register(self, *details):
		
		if len(details) == 1:
			print("Name :",details[0])

		elif len(details) == 2:
			print("Name :",details[0])
			print("Age :",details[1])

		elif len(details) == 3:
			print("Name :",details[0])
			print("Age :",details[1])
			print("Disease :",details[2])

p = Patient()

p.register("Anu")
print()
p.register("Ravi", 25)
print()
p.register("Meena", 30, "Diabetes")


print("\nMethod Overloading........")
print()

class Patient:

	def register(self, name, age = None, disease = None):
		print("Name :",name)

		if age is not None:
			print("Age :",age)

		if disease is not None:
            		print("Disease :", disease)

p = Patient()

p.register("Anu")
print()
p.register("Ravi", 25)
print()
p.register("Meena", 30, "Diabetes")





