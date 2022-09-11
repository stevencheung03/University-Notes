class Student:
	def __init__(self, name, idnumber):
		self.StudentName = name
		self.studentID = idnumber

	def display(self, StudentAge, StudentMarks):
		print("The student: ", self.StudentName, ", ID Number: ", self.studentID, ", Age : ", StudentAge, ", Mark: ", StudentMarks)

	def setAge(self, age):
		StudentAge = age
	
	def setMarks(self, marks):
		StudentAge = marks

reza = Student("reza", "ID123")

age = reza.setAge(30)

marks = reza.setMarks(100)

reza.display(age, marks)