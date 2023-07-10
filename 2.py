#We will be iterating through the Fibonacci sequence until we reach above 4 million, summing even numbers in the sequence along the way.

a = 1
b = 2
c = 0
total = 2

while True:
    c = a+b
    if 4000000<c:
        break
    else:
        a = b
        b = c
        if c%2==0:
            total+=c

print(total)
