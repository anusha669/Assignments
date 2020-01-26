fib=0
f1=0
f2=1
print(f1,f2,end=" ")
while fib <34:
    fib=f1+f2
    print(fib,end=" ")
    f1=f2
    f2=fib

# o/p: 0 1 1 2 3 5 8 13 21 34
# o/p: 0 1 1 2 3 5 8 13 21  while (fib+f2):