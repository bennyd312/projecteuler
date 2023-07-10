#We want to sum all multiples of 3 and 5 below 1000
#Idea: We will put all multiples of 3 and 5 below 1000 into a set and then use the sum() function
#The time complexity will be 2n=n, where n is the upper bound number



multiples = set()
numbers = [3,5]

for i in numbers:
    j=1
    while True:
        a = i*j
        if a < 1000:
            multiples.add(a)
            j+=1
        else:
            break
            
print(sum(multiples))
    
