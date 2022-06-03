import time
start_time = time. time()
def pandigital3(n):
    #Turn the number into a string
    number = str(n)
    #What we expect, by the definition of a pandigit number 
    digits = [str(x) for x in range(1, len(number)+1)]
    #Check if the two are the same
    return set(number) == set(digits)
count=0
for n in range(10000000):
    if pandigital3(n)==True:
        count+=1
print(count)

print("--- %s seconds ---" % (time. time() - start_time))
