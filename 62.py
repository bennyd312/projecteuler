#https://projecteuler.net/problem=62

#We will iterate over all the numbers from 1,2,..., cube them, sort their digits from the smallest to the largest and store the sorted number as a dictionary key with the dictionary value being the cube
def sortnumber(number):
    digits = [int(i) for i in str(number)]
    tempdigits = sorted(digits,reverse=True)
    sorteddigits = [str(i) for i in tempdigits]

    newnumber = "".join(sorteddigits)
    newnumber = int(newnumber)

    return newnumber

cubes = dict()
keys = []
smallestcube = 0
i=1


while True:
    temp = i**3
    number = sortnumber(temp)
    
    if number not in keys:
        keys.append(number)
        cubes[number] = [i]
        i+=1
    elif len(cubes[number])==4:

        smallestcube = min(cubes[number])
        break
    else:
        cubes[number].append(i)
        i+=1
print(smallestcube**3)