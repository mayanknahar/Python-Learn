#days of month are written in the list
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

#function to find leap year having parameter year
def is_leap(year):
	a=year%4==0 and (year%100!=0 or year%400==0)
	return a

#function to find the number of days in the month using the list defined above
def no_days(year,month):

#checks for the no of month entered
	if not 0<month<=12:
		return 'invalid month'
#special case of feb is defined for the leap year
	if month==2 and is_leap(year): # checks for both the conditions
		return 29
	return days[month]

#above defined functions are called by providing required functions
print(is_leap(2018))
print(no_days(2016,2))