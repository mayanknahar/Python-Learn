# Comparison:
#Equal:                 ==
#Not Equal:             !=
#Greater:               >
#less:                  <
#Greater or Equal:      >=
#less or Equal:         <=
#Object Identity:       is

a=int(input("Enter any digit for output"))
if a>0 and a<=10:
    print("the number is smaller than 10")
elif a>10:
    print("the number is greater than 10")
else:
    print("the number is 0")


#Boolean:
#and
#or
#not
user='Admin'
logged=True
if user=='Admin' and logged:
    print("Welcome to the portal")
else:
    print("Bad credentials")