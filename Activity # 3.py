name = input("Enter your name:")
section = input("Enter your section:")
n = int(input("Enter a positive integer: "))
total_sum = 0

if n > 0:
    for number in range(1, 1 + n):
        total_sum += number
    print(f"The sum of all numbers from 1 to {n} is  = {total_sum}.")

else:
    print("I miss you ")
    print("ay mali haha")