# Slicing list and strings
mylist=[0,1,2,3,4,5,6,7,8,9]
#index  0 1 2 3 4 5 6 7 8 9
#     -10-9-8-7-6-5-4-3-2-1

#to slice a group of elements from list use list[start:end:step]
#start is inclusive but end is exclusive

print(mylist[5])		#prints the eleement at index 5
print(mylist[-5])		#prints the element at index -5
print(mylist[:])		#prints the elements from start to end
print(mylist[5:])		#prints the element starting from 5 till end
print(mylist[:9])		#prints the elements from start till end
print(mylist[2:-2])		#prints the elements from index 2 to -2
print(mylist[2:-1:2])	#prints the value from 2 to -1 index with a jump of 2
print(mylist[::-1])		#will reverse the list and print it


# Now we can do slicing of strings also

name='Mayank Nahar'
print(name)

#Reverse the name
print(name[::-1])

#Get the top Level value say 'har'
print(name[-3:])

#print the string without 'May'
print(name[3:])

#print tne string without 'May' from start and 'har' from last
print(name[3:-3])
