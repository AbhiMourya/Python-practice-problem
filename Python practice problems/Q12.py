def duplicate2(arr):
    for i in arr:
        if arr.count(i)==2:
            return(i)


arr=[1,6,8,3,11,23,34,56,65,5,43,21,5]
print(duplicate2(arr))