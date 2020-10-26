#UNIT3-LINEAR SEARCH

def search(arr, n, x): 

	for i in range (0, n): 
		if (arr[i] == x): 
			return i
	return -1

 
arr = list(map(int,input().split(" ")))

x = int(input("Enter the element you want to search: ")) 
n = len(arr)
result = search(arr, n, x) 
if(result == -1): 
	print("Element is not present in array") 
else: 
	print("Element is present at index", result+1)
   