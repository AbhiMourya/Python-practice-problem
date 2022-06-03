def prime(number):
    pr_lst=[]
    for num in range(2,number):
        for j in range(2,int(num/2)):
                if num%j==0:
                    break
        else:
             pr_lst.append(num)
    return pr_lst

n=int(input())
inp_lst=''
for i in range(n):
    inp_lst+=(str(prime(int(input()))))+'\n'
print(inp_lst)