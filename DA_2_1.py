import random
def isPrime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return 
    if num > 1:
        print(num,end=" ")

lst = []
for i in range(0,16):
    ele = random.randint(1,75)
    lst.append(ele)
lst.sort(reverse=True)
print(lst)
for x in lst:
    isPrime(x)

'''def descSort(lst,length = 16):
    for i in range(0,length-1):
        if lst[i] > lst[i+1]
            t = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = t
'''