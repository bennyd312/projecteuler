#Smallest multiple X
#We will construct X by iterating Y from 1 to 20, getting the prime factors for each Y and then by comparing these prime factors

def prime_factors(n): #this function will return a list of prime factors of n
    factors = [0]
    number = 2
    while True:
        if n==1:
            break
        elif n % number == 0:
            factors[number - 2]+=1
            n = n/number
        else:
            factors.append(0)
            number += 1
    return factors

numbers = []
length = 1

for i in range(2,21): #generates prime factors for each number from 2 to 20
    numbers.append(prime_factors(i))

for i in numbers: #here length is the largest number of factors out of all the prime factorizations
    if len(i)>length:
        length = len(i)

prime_factors = [0 for i in range(length)] #prime factorization of the smallest multiple will be here
number = 2


for i in numbers: #prime factorization of SM
    for j in range(len(i)):
        if i[j]>prime_factors[j]:
            prime_factors[j] = i[j]

smallest_multiple = 1 #multiplying the factors of SM
for i in range(length):
    if prime_factors[i]!=0:
        smallest_multiple*=(i+2)**prime_factors[i]

print(smallest_multiple)

