#https://projecteuler.net/problem=14

chains = {1:1} #We will save the length of each number we haven't seen before here and if in another calculation we encounter it we already know its length
number = 2

while number<1000001:

    keys = chains.keys()
    n = number
    sequence = [n]
    tail = 1

    if number not in keys:
        while n!=1:
            if n in keys:#If we calculated it before already
                tail = chains[n]
                
                break
            elif n%2==0: 
                n = n/2
                sequence.append(n)
            else:
                n = 3*n + 1
                sequence.append(n)

        length = len(sequence)
        
        for i in range(length): #If we encountered a new value, here we save its sequence length and mark it as a known value
            if sequence[length-1-i] not in keys:
                chains[sequence[length-1-i]] = tail+i

        number += 1
    else: #If the starting number is known, we just move on
        number+=1
        
        

    
longest_kc = [0,0]

for i in range(1,1000001): #We go through the whole list and find the longest chain
    if longest_kc[1]<chains[i]:
        longest_kc[0] = i
        longest_kc[1] = chains[i]
        
print(longest_kc)
