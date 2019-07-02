#break:  	it breaks out of the current loop whrn the conditions are meet
#continue:	it continues to iterate over the loop even after the condition is meet 


numbers=[1,2,3,4,5]
print("lets check for the break statement first")
for num in numbers:
	if num==3:
		print("found the number 3")
		break          			#the pointer moves out of the for loop
	print(num)
print ("lets check continue statement")
for i in numbers:
	if i==3:
		print("found the number 3")
		continue 				#the pointer continues to itterate over for loop
	print(i)


# use of predefined range() method
#range(0,n) will give values from 0-(n-1)
for y in range(1,11):
	print(y)


# In while loop the loop runs until the required condition is met
x=0
while x<10:
	print(x)
	x+=1


'''while True:
	if x==5:
		print("reached level 5")
		break 						#if break statement is not used it will be an infinite loop as the condition is always true
	print(x)
	x+=1'''