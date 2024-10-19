import time
import integerfactorizations as intfact

class detailednumber:
    def __init__(self,number,pfactorization=[[],[]], phi = None, known = False):

        self.number = number
        self.pfactorization = {}
        self.phi = None
        self.known = False
        
def anagramic(detailednumber):
    arg = [i for i in str(detailednumber.number)]
    fun = [i for i in str(detailednumber.phi)]
    arg.sort()
    fun.sort()
    result = True
    if len(arg) != len(fun):
        result = False
    else:
        for i in range(len(arg)):
            if arg[i] != fun[i]:
                result = False
                break

    
    return result


def primedecomposition(number):
    """
    Input: Number
    Output: Dict of prime numbers and their exponents
    
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
    output = {}
    for i in range(len(bases)):
        output[bases[i]] = exponents[i]

    return output

def expanddetailednumber(detailednumber):
    number = detailednumber.number

    for prime in primes:
        newnumber = number * prime

        if newnumber<limit:

            if detailednumbers[newnumber].known == False:
                newfactorization = detailednumbers[number].pfactorization.copy()
                detailednumbers[newnumber].pfactorization = newfactorization
                bases =  list(detailednumber.pfactorization.keys())

                if prime in bases:
                    detailednumbers[newnumber].pfactorization[prime] += 1
                else:
                    detailednumbers[newnumber].pfactorization[prime] = 1
                
                expanddetailednumber(detailednumbers[newnumber])
                detailednumbers[newnumber].known = True
                detailednumbers[newnumber].phi = relativeprimes(detailednumbers[newnumber])
                global minphi, minint

                if newnumber/detailednumbers[newnumber].phi < minint/minphi and anagramic(detailednumbers[newnumber])==True:
                    minphi = detailednumbers[newnumber].phi
                    minint = detailednumbers[newnumber].number
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
    bases = list(detailednumber.pfactorization.keys())
    
    for base in bases:
        result = result * (base**(detailednumber.pfactorization[base]-1))*(base-1)

    return result

start = time.time()
global primes, limit, minint, minphi

minphi = 1
minint = 10
limit = 10000000

detailednumbers = {}
for i in range(2,limit):
    detailednumbers[i] = detailednumber(i)

primes = intfact.sieve_erat(limit)

for prime in primes:
    detailednumbers[prime].pfactorization[prime] = 1
    detailednumbers[prime].known = True
    detailednumbers[prime].phi = prime - 1
    expanddetailednumber(detailednumbers[prime])
    if prime/detailednumbers[prime].phi < minint/minphi and anagramic(detailednumbers[prime])==True:
        minphi = detailednumbers[prime].phi
        minint = prime

for i in range(2,limit):
    if detailednumbers[i].known == True:

        #print(i,detailednumbers[i].pfactorization,detailednumbers[i].phi)
        continue
    else:
        primedecomp = primedecomposition(detailednumbers[i].number)
        detailednumbers[i].pfactorization = primedecomp
        detailednumbers[i].phi = relativeprimes(detailednumbers[i])
        if i/detailednumbers[i].phi < minint/minphi and anagramic(detailednumbers[i])==True:
            minphi = detailednumbers[i].phi
            minint = i
        expanddetailednumber(detailednumbers[i])
        #print(i,detailednumbers[i].pfactorization,detailednumbers[i].phi)

print(minint)
end = time.time()
print(end - start)