#https://projecteuler.net/problem=22

import inputreader as ir
import string

def evaluate(name,values,multiplier):
   score = 0

   for i in range(len(name)):
      score += values[name[i]]
    
   return score * multiplier 

score = 0
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1


text = ir.saveinput("0022_names")
text = text[0].replace('"','')
text = text.split(",")
text.sort()

for i in range(len(text)):
   temp = evaluate(text[i],values,i+1)
   score += temp

print(score)
