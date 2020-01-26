import random
def isPrime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return 
    if num > 1:
        print(num,end=" ")

lst = []
for i in range(0,16):
    lst.append(random.randint(1,75))
lst.sort(reverse=True)
print(lst)
for x in lst:
    isPrime(x)

'''
    def desc(lst):
    for i in range(0,15):
        for j in range(i+1,16):
            if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    print(lst)
'''
