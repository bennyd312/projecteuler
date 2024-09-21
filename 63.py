#https://projecteuler.net/problem=63
#we can see that from a certain point, there wont exist any positive integer satisfying the given conditions
digits = []
n=100
def checkdigits(exponent):
    totalintegers = []
    i=1

    while True:
        number = i**exponent
        digits = [i for i in str(number)]

        if exponent == len(digits):
            totalintegers.append(number)
            i+=1
        elif exponent < len(digits):
            break
        else:
            i+=1
    
    return totalintegers

for i in range(1,n+1):
    digits.append(len(checkdigits(i)))

print(sum(digits))