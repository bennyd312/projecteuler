#summation of primes
#reusing the same method from problem 7 is too inefficient.
#Instead, we will be using the sieve of eratosthenes algorithm

n=2000000
numbers = [i for i in range(2,n+1)]
primes = [True for i in range(2,n+1)]
p=2

while p<n+1:
    if primes[p-2]==True:
        for i in range(2*p,(n//p)*p+1,p):
            primes[i-2]=False
        p+=1
    else:
        p+=1

total = [numbers[i] for i in range(len(numbers)) if primes[i]==True]

print(sum(total))
