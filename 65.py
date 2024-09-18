#https://projecteuler.net/problem=65
#Using the fraction functions from problem 57, we will calculate the convergent from "inside out"

def fractionsum(number,nominator,denominator):
    new_denominator = nominator + number*denominator
    new_nominator = denominator

    return new_nominator, new_denominator

sequence = []
counter = 4
for i in range(99):
    if i==0:
        sequence.append(i+1)
    elif i==1:
        sequence.append(i+1)
    else:
        if (i-1)%3==0:
            sequence.append(counter)
            counter += 2
        else:
            sequence.append(1)
backwardssequence = [sequence[-i] for i in range(1,len(sequence)+1)]

convergent_frac = [1,backwardssequence[0]]

for i in range(1,len(backwardssequence)):
    new_nominator, new_denominator = fractionsum(backwardssequence[i],convergent_frac[0],convergent_frac[1])
    convergent_frac = [new_nominator,new_denominator]


convergent_frac[0] = convergent_frac[0]+2*convergent_frac[1]

print(sum([int(i) for i in str(convergent_frac[0])]))