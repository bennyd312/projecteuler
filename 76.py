#https://projecteuler.net/problem=76

partitions = {0:1,1:1,2:2,3:3,4:5}
number = 1

while number<101:
    if number in partitions:
        number += 1
    else:
        total = 0
        k=1
        while True:
            sequence = [int(k*(3*k-1)/2),int(-k*(-3*k-1)/2)]
            if number-sequence[0]<0:
                break
            else:
                for seq in sequence:
                    if seq>number:
                        break
                    else:
                        temp = partitions[number-seq]
                        if k%2==0:
                            total = total - temp
                        else:
                            total = total + temp
                k+=1

        partitions[number] = total
        number += 1

print(partitions[100]-1) #single number sol
        