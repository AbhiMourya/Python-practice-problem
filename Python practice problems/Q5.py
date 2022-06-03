def duplicate(arr):
    l=len(arr)
    for i in range(l):
        for j in range(i):
            if arr[i]==arr[j]:
                return arr[i]

arr1=[1,8,3,11,23,34,56,65,5,43,21,5]
print(duplicate(arr1))
