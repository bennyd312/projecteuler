#We want to find the largest palindromic number made from the product of two 3 digit numbers.
#Idea: We will fix a number X from (99,1000) and iterate through Y from (99,X], we will check if X*Y is palindromic, in which case we will put it into a list. Once done we will just pick the largest element from the list.
#It is enough to check number Y bounded by X, to avoid checking the same number twice.
palindromes = []

for i in range(999,99,-1):
    for j in range(i,99,-1):
        digits = [int(k) for k in str(i*j)]
        conditions = [digits[0]==digits[-1],digits[1]==digits[-2],digits[2]==digits[-3]]
        if all(conditions):
            palindromes.append(i*j)

print(max(palindromes))
