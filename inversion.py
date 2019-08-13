def getInvCount(arr, n): 
  count = 0
  for i in range(n): 
    for j in range(i + 1, n): 
      if (arr[i] > arr[j]): 
        count += 1
       
  return count
print("Count number of Inversions in a Given Array")
list=[]
n=int(input("Enter the number of elements to be present in the list "))
for i in range(0,n):
  s=int(input())
  list.append(s)
n = len(list) 
print("Number of inversions are",getInvCount(list, n))  
