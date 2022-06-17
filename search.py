#implement linear search function
def linear_search(arr,n,x):
    for i in range(len(arr)) :
        if(arr[i]==x):
            print("found at index",i)
            
       

#implement binary search

def binary_search(max, min ,arr, n ,x):
    mid = (max+min)//2
    if(arr[mid]==x):
        print("found at index",mid)
    elif(arr[mid]>x):
        binary_search(min,mid-1,arr,n,x)
    elif(arr[mid]<x):
        binary_search(mid+1,max,arr,n,x)
    else:
        print("not found")

print("Enter the list of numbers")
_list = list(int(x) for x in input().split())
print(_list)
print("Enter the number to be searched")
x = int(input())
print("finding",x)

print ("using binary search")
range = len(_list)
binary_search(range,0,_list,range,x)

print("using linear search")
linear_search(_list,range,x)
