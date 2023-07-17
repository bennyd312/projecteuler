#https://projecteuler.net/problem=17

values = {0:0 ,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8} #this dict will contain the word length of each digit
second = {2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
total = 0
#one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen
#twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety
def length(number):
    count = 0
    original = number%100
    number = [int(i) for i in str(number)]
    if len(number) == 3:
        count += values[number[0]] + 7 # x hundred
        if number[1] != 0 and number[1]!=1:
            count += second[number[1]] #2nd digit
            count += 3 #and
            count += values[number[2]]
        elif number[1]==0 and number[2]==0:
            pass
        else:
            count += values[original]
            count += 3
                    
    elif len(number)==2:
        if number[0]!=1:
            count += second[number[0]]
            count += values[number[1]]
        else:
            count += values[original]
    elif len(number)==4:
        count+=11 #one thousand 
    else:
        count += values[number[0]]
        
    return(count)
        
for i in range(1,1001):
    total += length(i)
