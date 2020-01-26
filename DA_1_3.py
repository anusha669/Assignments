n = int(input("Enter a number greater than 1: "))
sum = 0
while n>2:
    sum += 1/pow(n,3)
    n -=1
print(f"Result : {sum}")