#https://projecteuler.net/problem=59
"""
Every third character is encrypted with the same lower case letter.
Using frequency analysis we can count the most common value for each value with the same key and guess its decrypted value
Since we are considering a normal text, we can guess that the most used character is space
"""
def binarydecomp(number):
    """
    Binary decomposition for numbers from [0,127]
    """
    byte = [0,0,0,0,0,0,0,0]
    divisor = 64
    for i in range(7):
        bit = number//divisor
        number = number % divisor
        divisor = divisor / 2 
        byte[i+1] = int(bit)
    
    return byte
def binaryrecomp(exponents):
    number = 0
    for i in range(7):
        number = number + exponents[i+1]*(64/(2**i))
    return int(number)

def frequency(numbers):
    most_frequent_number = 0
    frequency = 0
    numberfrequence = {}
    for i in numbers:
        if i in numberfrequence.keys():
            numberfrequence[i] += 1
        else:
            numberfrequence[i] = 1

    for key in numberfrequence.keys():
        if numberfrequence[key] > frequency:
            most_frequent_number = key
            frequency = numberfrequence[key]
    
    return most_frequent_number




import inputreader as ir
#note: I lost the previous inputreader from some of the previous problems. This one does +- the same thing, but it probably won't work for the earlier problems anymore

text = ir.saveinput("0059_cipher")
spacebyte=[0,0,1,0,0,0,0,0]
text = text[0].split(",")
text = [int(i) for i in text]
decryptedtext = []

first = [] #every first number in a triple
second = [] #every second number in a triple
third = [] #every third number in a triple

for i in range(len(text)):
    if i%3==0:
        first.append(text[i])
    elif i%3==1:
        second.append(text[i])
    else:
        third.append(text[i])

frequency1 = frequency(first)
frequency1 = binarydecomp(frequency1)
key1 = [(spacebyte[i]+frequency1[i])%2 for i in range(8)] #we will keep the keys stored as binary numbers, since we are going to need them to decrypt the messages anyways

frequency2 = frequency(second)
frequency2 = binarydecomp(frequency2)
key2 = [(spacebyte[i]+frequency2[i])%2 for i in range(8)]

frequency3 = frequency(third)
frequency3 = binarydecomp(frequency3)
key3 = [(spacebyte[i]+frequency3[i])%2 for i in range(8)]

for i in range(len(text)):
    if i%3==0:
        temp = binarydecomp(text[i])
        value = [(temp[j]+key1[j])%2 for j in range(8)]
        decryptedtext.append(binaryrecomp(value))
    elif i%3==1:
        temp = binarydecomp(text[i])
        value = [(temp[j]+key2[j])%2 for j in range(8)]
        decryptedtext.append(binaryrecomp(value))
    else:
        temp = binarydecomp(text[i])
        value = [(temp[j]+key3[j])%2 for j in range(8)]
        decryptedtext.append(binaryrecomp(value))

print(sum(decryptedtext))
