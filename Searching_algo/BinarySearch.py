arr=list(map(int,input().split()))
num=int(input("Enter the element you want to search: "))
pos=-1

def Binary_Search(arr,n):
    L=0     #L is Lower bound
    U=len(arr)  #U is upper bound
    
    while L<=U:
        mid=(L+U)//2
        if arr[mid]==num:   #checks if the element is present in the mid of the arr
            globals()['pos']=mid
            return True
        else:
            if arr[mid]>num:   
                U=mid-1
                mid=(L+U)//2
            else:
                L=mid+1
    return False              

if Binary_Search(arr,num):
    print("Element found at : ",pos+1)
else:
    print("Element is not present in the list.")                              