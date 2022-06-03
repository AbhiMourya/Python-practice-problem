def sum_int(str):
    sum=0
    for i in str:
        if i.isdigit():
            sum+=int(i)
    return sum

print(sum_int('hj325436ji5nt'))