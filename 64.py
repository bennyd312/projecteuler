#https://projecteuler.net/problem=64

def simplify_frac(nominator, denominator):
    i = 2
    while i < min(nominator, denominator) + 1:
        if nominator % i == 0 and denominator % i == 0:
            nominator = nominator // i
            denominator = denominator // i
        else:
            i += 1
    return nominator, denominator

def expandsqrt(denominator,squaredroot,nominator=1):


    
    newdenominator = (squaredroot - denominator[1]**2)

    coef1, coef2 = simplify_frac(nominator,newdenominator)
    
    newdenominator = coef2
    newnominator = [denominator[0]*coef1,-denominator[1]*coef1]

    return newnominator,newdenominator

def removewholenumberpart(nominator,denominator):

    whole = int((nominator[0]+nominator[1])/(denominator))

    nominator[1] = nominator[1] - whole*denominator

    return nominator, whole

def continued_fraction(number):
    sqrt = number **(1/2)
    sequence = []
    remainders = []
    result = []

    first = int(sqrt)
    result.append(first)

    coef = 1
    nominator = [sqrt,-first] # nominator = sqrt + wholenumberpart

    while True:
        

        newnominator, newdenominator = expandsqrt(nominator,number,coef)
        newnominator, whole = removewholenumberpart(newnominator,newdenominator)

        sequence.append(whole)
        remainders.append([newnominator,newdenominator])

        nominator = newnominator
        coef = newdenominator
        maxindex = len(sequence)
        if sequence[0:maxindex//2]==sequence[maxindex//2::]:
            
            if remainders[0:maxindex//2]== remainders[maxindex//2::]:
                result.append(sequence[0:maxindex//2])
                break
    
    return result

squares = []
n=2 
counter = 0

while True:
    square = n*n
    squares.append(square)
    if square>10000:
        break

    else:
        n+=1

for i in range(2,10001):

    if i not in squares:

        if len(continued_fraction(i)[1])%2==1:
            counter+=1

print(counter)