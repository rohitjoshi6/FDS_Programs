def insertionSort(arr):
   for i in range(1,len(arr)):

     currentvalue = arr[i]
     position = i

     while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1
         #print(arr)

     arr[position]=currentvalue

arr = list(map(int,input().split(" ")))
insertionSort(arr)
print(arr)
