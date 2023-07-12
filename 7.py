#10001st prime
primes = [2]
number = 3

while len(primes)<10001:
    prime = True
    for i in primes:
        if number % i == 0:
            prime = False
            break
    if prime==True:
        primes.append(number)
        number+=1
    else:
        number+=1
print(primes[-1])
