def sieve_erat(number):
    usage = {}
    factorization = {}

    for i in range(2,number+1):
        usage[i] = True

    values = list(usage.keys())

    for i in values:

        j=2

        if i%2==0:
            if i==2:
                while True:

                    if 2*j<=number:
                        usage[2*j] = False
                        j+=1

                    else:
                        break
        
        else:
            j=3

            while True:

                if i*j<=number:
                    usage[i*j] = False
                    j+=2

                else:
                    break


    primes = [number for number in values if usage[number]==True]
    return primes



def applied_erat(number):
    #needs a rework, redundant code
    """
    Using sieve of eratosthenes to get prime number factorization
    Time complexity is (n*log(log(n))) ... pseudopolynomial ?
    """
    usage = {}
    factorization = {}

    for i in range(2,number+1):
        usage[i] = True

    values = list(usage.keys())

    for i in values:

        j=2

        if i>=number**(1/2):
            break

        elif i%2==0:
            if i==2:
                while True:

                    if 2*j<number:
                        usage[2*j] = False
                        j+=1

                    else:
                        break
        
        else:
            j=3

            while True:

                if i*j<number:
                    usage[i*j] = False
                    j+=2

                else:
                    break

    temp = number
    index = 0
    
    while temp != 1:
        
        value = values[index]

        if usage[value] == True:
            if temp % value == 0:
                
                if value in factorization.keys():
                    factorization[value] += 1
                    temp = temp // value

                else:
                    factorization[value] = 1
                    temp = temp // value
            else:
                index += 1
        else:
            index += 1
    bases = list(factorization.keys())
    exponents = []

    for base in bases:
        exponents.append(factorization[base])
        
                



    return bases, exponents


def recomposition(bases,exponents):
    
    number = 1
    for i in range(len(bases)):
        number = number * bases[i]**exponents[i]

    return number