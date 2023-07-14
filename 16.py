#https://projecteuler.net/problem=16
number = [2]
for i in range(1,1000):
    temp = number
    for j in range(len(number)):
        number[j]*=2
    for j in range(len(number)):
        if number[j]>9:
            if j>=len(number)-1:
                number.append(number[j]//10)
                number[j]-= 10*(number[j]//10)
            else:
                number[j+1] += number[j]//10
                number[j] -= 10*(number[j]//10)

print(sum(number))
