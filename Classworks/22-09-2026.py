#OOP's

class Account: #empty type
	pass

type(Account)

a1 = Account()
a2 = Account()
a1.name = "John"
a1.balance = 1000

a2.surname = "Maria"
a2.value = 100010
a2.balance = 1200

print(id(Account))

print(a2)
print(a1.balance)
#print(a1.surname) AttributeError: 'Account' object has no attribute 'surname'
print(a2.surname)

print("\n....................................")

print()

class Patient:

	def __init__(self, patient_id, name, age, diagnosis):
		self.patient_id = patient_id
		self.name = name
		self.age = age
		self.diagnosis = diagnosis

	def display(self):
		print("Patient ID: ",self.patient_id)
		print("Name: ",self.name)
		print("Age: ",self.age)
		print("Diagnosis: ",self.diagnosis)

	def is_senior(self):
		return self.age >= 60

p1 = Patient("P101", "Ananya", 35, "Diabetes")
p2 = Patient("P102", "Ravi", 67, "Hypertension")

p1.display()
print("Senior: ",p1.is_senior())

print()

p2.display()
print("Senior: ",p2.is_senior())

print("\n....................................")
print()

#Create a class student with three methods 1.Calculate total and average 2. display student details 3.display pass or fail

class Student:

	@staticmethod
	def colege_name():
		print("Christ University")

	def __init__(self, student_id, name, m1, m2, m3):
		self.student_id = student_id
		self.name = name
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
		self.total = self.m1 + self.m2 + self.m3
		self.average = self.total / 3
		self.result = self.average
		
	def display(self):
		print("Studnet ID: ",self.student_id)
		print("Name: ",self.name)
		print("Marks 1: ",self.m1)
		print("Marks 2: ",self.m2)
		print("Marks 3: ",self.m3)
		print("Total: ",self.total)
		print("Average: ",round(self.average, 2))

	def is_result(self):
		if self.result >= 40:
				     return "Pass"
		else:
		     return "Fail"


s1 = Student("S101", "Ananya", 41, 42, 44)
s2 = Student("S102", "Ravi", 5, 3, 2)

Student.colege_name()
print()

s1.display()
print("Result: ",s1.is_result())

print()

s2.display()
print("Result: ",s2.is_result())

print("\nClass Method....................................")
print()

class Patient:
	hospital_name = "ABC Hospital"
	
	@classmethod
	def display_hospital(cls):
		print(cls.hospital_name)

Patient.display_hospital()


print("\nStatic Method....................................")
print()


class Patient:
	
	@staticmethod
	def hospital_timings():
		print("Hospital Timing: 9 AM - 5 PM")

Patient.hospital_timings()

print("\nSingle Inheritance....................................")
print()

class Patient:
	def show_patient(self):
		print("Patient ID: P101")
		print("Name: Ananya")

class InPatient(Patient):
	def show_room(self):
		print("Room Number: 205")

patient = InPatient()

patient.show_patient()
patient.show_room()

print("\nMultiple Inheritance....................................")
print()

class Patient:
	def patient_details(self):
		print("Patient Name: Ananya")

class Billing:
	def billing_details(self):
		print("Consultaion Fee: 500")

class HospitalRecord(Patient, Billing):
	def record_details(self):
		print("Hospital Record Generated")

record = HospitalRecord()

record.patient_details()
record.billing_details()
record.record_details()

print("\nMultilevel Inheritance....................................")
print()

class Patient:
	def patient_details(self):
		print("Patient Name: Ananya")

class Billing(Patient):
	def billing_details(self):
		print("Consultaion Fee: 500")

class HospitalRecord(Billing):
	def record_details(self):
		print("Hospital Record Generated")

record = HospitalRecord()

record.patient_details()
record.billing_details()
record.record_details()

print("\nhierarchical Inheritance....................................")
print()

class Patient:
	def patient_details(self):
		print("Patient Name: Ananya")

class Billing(Patient):
	def billing_details(self):
		print("Consultaion Fee: 500")

class HospitalRecord(Billing):
	def record_details(self):
		print("Hospital Record Generated")

record = HospitalRecord()

record.patient_details()
record.billing_details()
record.record_details()

