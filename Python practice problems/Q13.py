def odd_count(lst):
    for i in lst:
        if lst.count(i)%2!=0:
            return i

lst=[2,2,3,3,4,4,4,4,5,5,5,6,6,7,7,8,8]
print(odd_count(lst))