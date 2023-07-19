#maximum path sum
#We will solve this problem using classes.
import inputreader as ir 

lines = ir.readinput()
rows = []
for line in lines:
    a = line
    a = [int(i) for i in a.split(" ")]
    rows.append(a)
    
distance = rows

for row in range(len(rows)-1,0,-1):
    for column in range(len(rows[row])-1):
        if rows[row][column] > rows[row][column+1]:
            distance[row-1][column] += rows[row][column]
        else:
            distance[row-1][column] += rows[row][column+1]

        

