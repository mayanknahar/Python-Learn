print("program for insertion sort")
list=[]
n=int(input("Enter the number of elements to be sorted  "))
for i in range(0,n):
  s=int(input())
  list.append(s)
print(list)
for j in range(1,len(list)):
  key=list[j]
  i=j-1
  while i>=0 and list[i]>key:
    list[i+1]=list[i]
    i=i-1
  list[i+1]=key
print(list)