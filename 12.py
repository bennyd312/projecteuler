#https://projecteuler.net/problem=12
#We will find the prime factorization of each triangular number and from that we easily calculate how many divisors it has using the product of its exponents.
#We improve factorization speed by factoring out all the 2's and then checking the rest of the prime numbers, which will be odd.

def prime_factorization(number):
    primes = [2]
    exponents = [0]
    p = 2
    index = 0
    while number%2==0:
        exponents[0] += 1
        number = number / 2

    sqrt = int(number**(1/2))
    for i in range(3,sqrt+1,2):
        if number%i==0:
            primes.append(i)
            exponents.append(0)
            index += 1
            
        while number%i==0:
            number = number / i
            exponents[index]+= 1

    return exponents
        
            
    """
    while number != 1:
        conditions = [p % i !=0 for i in primes]
        if all(conditions):
            primes.append(p)
            exponents.append(0)
            while number % p == 0:
                number = number / p
                exponents[index]+=1
            if p == 2:
                p+=1
            else:
                p+=2

            index+=1
        else:
            p+=1
    return exponents
    """


value = 1
n = 2
tick = 0

while True:
    current_divisors = 1
    trianglenum = int(n*(n+1)/2)
    temp = [i for i in prime_factorization(trianglenum) if i!=0]
    for i in temp:
        current_divisors*=i+1
    if 500<current_divisors:
        value = trianglenum
        break
    elif tick==1000:
        print(trianglenum,current_divisors)
        tick=0
    n+=1
    tick+=1

print(value)
