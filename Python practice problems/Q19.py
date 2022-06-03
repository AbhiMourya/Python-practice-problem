from random import randint as rd
ans=str(rd(1000,10000))
def game(ans):
    user=input()
    while ans!= user:
        check=''
        for i in range(4):

            if ans[i]==user[i]:
                check+="R"
            elif user[i] in ans:
                check+='B'
            else:
                check+='Y'
        print(check)
        user=input()
    print('You win!!! \nAnswer is',ans)

game(ans)