from abc import ABC, abstractmethod

class Patient(ABC):

	def __init__(self, patient_id, name):
		self.patient_id = patient_id
		self.name = name

	def display_name(self):
		print("Patient ID: ", self.patient_id)
		print("Patient Name: ", self.name)

	@abstractmethod
	def treatment(self):
		pass

class CardiacPatient(Patient):

	def treatment(self):
		print("Treatment: Cardiac Care")

class OrthopediacPatient(Patient):
	
	def treatment(self):
		print("Treatment: Orthopediac Care")

class DiabetesPatient(Patient):
	
	def treatment(self):
		print("Treatment: Diabetic Care")

p1 = CardiacPatient(101, "Anu")
p2 = OrthopediacPatient(102, "Ravi")
p3 = DiabetesPatient(103, "Meena")

print("\nAbstract Method..............")
print()

p1.display_name()
p1.treatment()
print()
p2.display_name()
p2.treatment()
print()
p3.display_name()
p3.treatment()