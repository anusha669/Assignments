def isPrime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return False
    return True

def sum(lst):
    sum = 0
    for ele in lst:
        sum += ele
    print(f"Sum = {sum}")

def square(lst):
    sq_lst = []
    for ele in lst:
        sq_lst.append(ele*ele)
    print(f"Squared List: {sq_lst}")

n = int(input("Enter a number: "))
lst = []
for i in range(2,n):
    flag = isPrime(i)
    if flag == True:
        lst.append(i)
lst.sort()
sum(lst)
square(lst)