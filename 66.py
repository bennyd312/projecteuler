#https://projecteuler.net/problem=66
#In the commented code at the bottom I tried solving directly - too slow
#After researching the problem is called Pell's equation and we can solve it using continued fractions from previous problems, namely problem 64
#Created a new module called 'fractions.py' to keep the code more comprehensible.
#We will find the fundamental solution to Pell's equation using the method described in 
#https://brilliant.org/wiki/quadratic-diophantine-equations-pells-equation/#fundamental-solution


import fractions as fr
squares = []
D=2
i=1
base = 0

largest = 0
key = 2

while True: #make a list of all numbers that are squares - so we can avoid them
    val = i*i

    if val>1001:
        base = i
        break
    else:
        i+=1
        squares.append(val)


while D<1001:

    if D in squares:
        D+=1

    else:
        x ,y = 0, 0
        continuedfraction = fr.continued_fraction(D)
        sequence = []
        sequence.append(continuedfraction[0])

        for i in continuedfraction[1]:
            sequence.append(i)
        
        if len(continuedfraction[1])%2==0:
            sequence.pop()
            x,y = fr.reducefraction(sequence)

            if x>largest:
                key = D
                largest = x

            D+=1


        else:

            for i in range(len(continuedfraction[1])-1):
                sequence.append(continuedfraction[1][i])
            
            x,y = fr.reducefraction(sequence)

            if x>largest:
                key = D
                largest = x
            D+=1
        
print(key)



#following code doesnt work, directly trying to find smallest x is too slow
"""
while D<1001:
    #print(D)
    if D in squareskeys:
        D+=1
    else:
        j=1 

        while True:
            ysquare = j
            if ysquare in squareskeys:
                xsquare = j*D+1
                if xsquare in squareskeys:
                    print(squares[xsquare],D,squares[ysquare])
                    Dvalues[D] = squares[xsquare]
                    D+=1
                    break
                else:
                    if xsquare<maxsquare:
                        j+=1
                    else:
                        base += 1
                        maxsquare = base * base
                        squareskeys.append(maxsquare)
                        squares[maxsquare] = base
            else:
                if ysquare<maxsquare:
                    j+=1
                else:
                    base += 1
                    maxsquare = base*base
                    squareskeys.append(maxsquare)
                    squares[maxsquare] = base
"""