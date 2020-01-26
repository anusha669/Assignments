num = int(input("Enter number"))
rem = 0
while True:
    while num>0:
        rem += num%10
        num = num/10
    if rem < 10:
        break
    num = rem
print(f"The result is {num}")



'''cp = int(input("Cost price"))
sp = int(input("Selling price"))
if sp>cp:
    print("Profit")
else:
    print("Loss")
diff = abs(sp-cp)
print(f"Quantum of profit or loss is {(diff/cp)*100}")'''
