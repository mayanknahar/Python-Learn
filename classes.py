# Concept of classes and instances

class Employee:								#class employee is defined using the keyword class
											#self is for the instance 
	def __init__(self,first,last,pay):		#init method is to initialise the values of the class or instances created
		self.first=first					#assigns the value taken as parameter to the class value
		self.last=last
		self.pay=pay
		self.email=first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


emp1=Employee('Mayank','Nahar',60000)		#instance of the class is created with the values
											#self is not sent as a parameter as it is by default sent to the init method here self is emp1
emp2=Employee('Rahul','kumar',50000)
print(emp1)
print(emp2)
print(emp2.email)
print(emp1.fullname())
print(Employee.fullname(emp1))			#if we call the function of the class using the class name then we need to send the self manually