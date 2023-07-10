#We want to find the largest prime factor of number X.
#Idea: If X is divisible by Y, then X % Y = 0. We will be generating prime numbers as follows: A is prime if for all B prime, B<A => A % B != 0, then we will check if X % A = 0. If so, then A is a prime factor of X.

numberinput = 600851475143 
primes = [2]
prime_factors = []
number = 2 # first prime number
largest_prime_factor = 0


if numberinput%number==0:
    prime_factors.append(number)

while True:
    number+=1

    if all([True for i in primes if number%i==0]):
        primes.append(number)
        if numberinput % number == 0:
            print(number)
            prime_factors.append(number)
            total = 1
            for i in prime_factors:
                total = total*i
            if numberinput == total:
                largest_prime_factor = max(prime_factors)
                break
print('End')

