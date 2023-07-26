#https://projecteuler.net/problem=20

number = [1] #here we store the factorial with each of its digits as a list element (in reverse)
current = 1

while current<101:
    index = 0
    for i in range(len(number)):
        number[i]*=current

    
    while True:
        if number[index]//10==0 and index == len(number) - 1:
            break
        elif number[index]//10!=0:
            if index == len(number) - 1:#avoid running out of index
                number.append(0)
            number[index+1] += number[index]//10
            number[index] -= (number[index]//10)*10
            index+=1
        else:
            index+=1
    current += 1


print(sum(number))
