def prime(a,b):
    if a < 0: a = 0
    if a > b: a,b=b,a
    pr_lst=[]
    if b>=a:
        for num in range(a,b+1):
            for j in range(2,int(num/2)):
                if num%j==0:
                    break
            else:
                if num not in (0,1):
                    pr_lst.append(num)
        return pr_lst
    else:
        print('Incorrect input!!!')

print(prime(1,40))
print(prime(30,10))
print(prime(-23,20))
