def highest_freq(lst):
    max=0
    for i in lst:
        freq=lst.count(i)
        if freq >= max:
            if freq==max:
                element.add(i)
            else:
                max=freq
                element= {i}
    return element

lst=[1,3,2,4,5,2,1,3,2,4,5,2,6,6,6,6]
lst1=[1,3,2,4,5,2,1,3,2,4,5,2,6,6,6]
print(highest_freq(lst))
print(highest_freq(lst1))

