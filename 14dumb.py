#14

longest_kc = [0,0]

for i in range(1,1000001):
    num = i
    sequence = [i]
    while i!=1:
        if i%2==0:
            i=i/2
            sequence.append(i)
        else:
            i=3*i+1
            sequence.append(i)
    length = len(sequence)+1
    if longest_kc[1]<length:
        longest_kc[1] = length
        longest_kc[0] = num
