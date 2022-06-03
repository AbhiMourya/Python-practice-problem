def calc(a,o,b):
    # calc_str=str(a)+o+str(b)
    # ans=eval(calc_str)
    # return ans
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        if b==0:
            return "Not defined"
        else:
            return a/b


print(calc(4,"-",7))
print(calc(4,'+',6))
print(calc(3,'*',5))
print(calc(16,'/',3))
print(calc(3,'/',0))
