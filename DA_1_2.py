# from time import process_time
# start = process_time()
num = input("Enter a number:")
sum = 0
for dig in num:
    sum += int(dig)
print(f"Sum of digits : {sum}")

''' while(num != 0):
        sum += num%10
        num = num//10 '''

# end = process_time()
# print(end,start)