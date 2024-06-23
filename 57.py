#problem57
#https://projecteuler.net/problem=57

def fractionsum(number,nominator,denominator):
    new_denominator = nominator + number*denominator
    new_nominator = denominator

    return new_nominator, new_denominator

def evaluatefraction(nominator,denominator):
    if len(list(str(nominator)))>len(list(str(denominator))):
        return 1
    else:
        return 0


i=1
counter = 0

nominator = 1
denominator = 2

while i<1001:
    if i==1:
        evaluatefraction(nominator+denominator,denominator)
        i += 1
    else:
        nominator, denominator = fractionsum(2,nominator,denominator)
        final_denominator, final_nominator = fractionsum(1,nominator,denominator)
        if evaluatefraction(final_nominator,final_denominator)==1:
            counter += 1
        i += 1

print(counter)
