import time
import integerfactorizations as intfact

class detailednumber:
    def __init__(self,number,pfactorization=[[],[]], phi = None, known = False):

        self.number = number
        self.pfactorization = [[],[]]
        self.phi = None
        self.known = False
        


def primedecomposition(number):
    """
    Input: Number, list of all primes containing the input number
    Output: List of prime numbers and their exponents
    
    """
    temp = number
    bases = []
    factorization = {}

    index = 0

    while temp != 1:
        prime = primes[index]
        if temp%prime==0:
            if prime in bases:
                factorization[prime] += 1
                temp = temp // prime
            else:
                bases.append(prime)
                factorization[prime] = 1
                temp = temp // prime
        else:
            index += 1

    exponents = [factorization[base] for base in bases]

    return bases, exponents

def expanddetailednumber(detailednumber):
    number = detailednumber.number
    bases, exponents = detailednumber.pfactorization[0], detailednumber.pfactorization[1]

    for i in range(len(exponents)):
        newexponents = exponents.copy()
        newexponents[i] += 1
        newnumber = number * bases[i]

        if newnumber<limit:
            if detailednumbers[newnumber].known == False:
                detailednumbers[newnumber].pfactorization = [bases,newexponents]
                expanddetailednumber(detailednumbers[newnumber])
                detailednumbers[newnumber].known = True
                detailednumbers[newnumber].phi = relativeprimes(detailednumbers[newnumber])
                global maxphi
                if detailednumbers[newnumber].phi > maxphi:
                    maxphi = detailednumbers[newnumber].phi
                    maxint = detailednumbers[newnumber]
        else:
            break

def relativeprimes(detailednumber):
    """
    x,y positive integers. y is a relative prime of x if y=1,y=x or x%y != 0.
    Input: bases and exponents of prime factorization of a number
    Output: Number of all relative primes of x

    Using abstract algebra theory for divison, we can compute value of phi directly from the prime number factorization of the given number
    """
    result = 1
    bases = detailednumber.pfactorization[0]
    exponents = detailednumber.pfactorization[1]
    
    for i in range(len(bases)):
        result = result * (bases[i]**(exponents[i]-1))*(bases[i]-1)

    return detailednumber.number/result

start = time.time()
global primes, limit, maxint, maxphi

maxphi = 0
maxint = 0
limit = 1000000
detailednumbers = {}
for i in range(2,limit):
    detailednumbers[i] = detailednumber(i)

primes = intfact.sieve_erat(limit)

for prime in primes:
    detailednumbers[prime].pfactorization = [[prime],[1]]
    detailednumbers[prime].known = True
    detailednumbers[prime].phi = prime / (prime - 1)


for i in range(2,limit):
    if detailednumbers[i].known == True:
        if i%25000==0:
            print(i)
        continue
    else:
        primedecomp = primedecomposition(detailednumbers[i].number)
        bases, exponents = primedecomp[0], primedecomp[1]
        detailednumbers[i].pfactorization = [bases,exponents]
        detailednumbers[i].phi = relativeprimes(detailednumbers[i])
        if detailednumbers[i].phi > maxphi:
            maxphi = detailednumbers[i].phi
            maxint = i
        expanddetailednumber(detailednumbers[i])
        if i%25000==0:
            print(i)



"""
for no in range(2,limit):
    print(detailednumbers[no].number,detailednumbers[no].pfactorization)
"""
print(maxint)
end = time.time()
print(end - start)