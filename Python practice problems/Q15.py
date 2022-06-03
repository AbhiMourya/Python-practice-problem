def count_nac(str):
    num,alp,chr=0,0,0
    for i in str:

           if i.isdigit()==True:
               num+=1
           elif i.isalpha() == True:
               alp += 1
           else:
               chr+=1
    print('Digits:',num)
    print("Alphabets:",alp)
    print("Characters:",chr)


count_nac('ansj123;[/.,]jncs)')