#https://projecteuler.net/problem=21
#brute force solution

total = 0
numbers = {}

def amicablesum(number):
    divisors = []
    for i in range(1,number):
        if number%i==0:
            divisors.append(i)
    return sum(divisors)

for i in range(1,10001):
    value = amicablesum(i)
    numbers[i] = value
    if value<i:
        if value in numbers.keys():
            if numbers[value] == i:
                total+=i+value
                print(value,i)

print(total)


        
        
