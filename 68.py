#https://projecteuler.net/problem=68

#Number 10 may appear ONLY in the external nodes, otherwise the string would be too long.
#We will take all permutations of 1 to 9 using the permutationset() function
#For each permutation, number 10 must be an external node, and it cant be the node with the smallest value, therefore it has only 4 possible index values.
#We will transform the permutation to a number

import permutationset as ps

def joindigits(listofnumbers):

    return int("".join([str(digit) for digit in listofnumbers]))

def assignvalues(x): #assign value to the given permutations of numbers 1-10
    value = [x[0],x[1],x[2],
             x[3],x[2],x[4],
             x[5],x[4],x[6],
             x[7],x[6],x[8],
             x[9],x[8],x[1]]
    
    return joindigits(value)

def magic(x): #check if the 5-gon lines have all the same sum

    total = x[0] + x[1] + x[2]

    if x[3] + x[2] + x[4] != total:

        return False
    
    elif x[5] + x[4] + x[6] != total:

        return False
    
    elif x[7] + x[6] + x[8] != total:

        return False
    
    elif x[9] + x[8] + x[1] != total:

        return False
    
    else:

        return True

numbers = [i for i in range(1,10)]

permutations = ps.permutationset(numbers)
maxval = 0

for permutation in permutations:
    x = permutation.copy()
    externalnodes = [3,5,7,9]
    for i in externalnodes:
        tempperm = x.copy()
        tempperm.insert(i,10)
        externalvalues = [tempperm[i] for i in externalnodes]

        if tempperm[0] > min(externalvalues):
            continue
        else:
                

            value = assignvalues(tempperm)
            check = magic(tempperm)
            if check == True:
                if value > maxval:
                    maxval = value
print(maxval)
