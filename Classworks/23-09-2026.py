# Polymorphism

print("\nPolymorphism through method overriding..............")
print()

class Patient:

	def consultation(self):
		print("General Consultation")

class CardiologyPatient(Patient):
	
	def consultation(self):
		print("Cardiology consultation")

class OrthopedicPatient(Patient):

	def consulation(self):
		print("Orthopedic consultation")

p1 = CardiologyPatient()
p2 = OrthopedicPatient()

p1.consultation()
p2.consultation()

print("\nPolymorphism with a Common Interface..............")
print()

class Patient:

	def treatment(self):
		print("General treatment")

class DiabetesPatient(Patient):
	
	def treatment(self):
		print("Diabetes Management")

class HeartPatient(Patient):

	def treatment(self):
		print("Cardiac treatment")

patients = [DiabetesPatient(),HeartPatient(),Patient()]
for patient in patients:
	patient.treatment()

print("\nPolymorphism with different classes..............")
print()

class Doctor:

	def work(self):
		print("Doctor treats patients")

class Nurse:
	
	def work(self):
		print("Nurse provides patient care")

class Pharmacist:

	def work(self):
		print("Pharmacist provides medicines")

patients = [Nurse(),Pharmacist(),Doctor()]

for patient in patients:
	patient.work()


