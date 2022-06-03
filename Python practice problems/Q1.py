def arange(input_lst,method):
    if method=='asc':
        lst=sorted(input_lst)
    elif method=="des":
        lst = sorted(input_lst,reverse=True)
    elif method=='none':
        lst=input_lst
    print(lst)

arange([35,65,87,54,7,6,8,57,68,76,45],'asc')
arange([35,65,87,54,7,6,8,57,68,76,45],'des')
arange([35,65,87,54,7,6,8,57,68,76,45],'none')