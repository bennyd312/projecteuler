#https://projecteuler.net/problem=67
#Starting from the second to last row, we will look at each element, look at the two lower connected elements and add the higher one to the current element
#We will apply this process all the way to the "tip" of the pyramid, which will give us the maximum path sum
import inputreader as ir

pyramid = ir.saveinput("0067_triangle")

for i in range(len(pyramid)):
    pyramid[i] = [int(j) for j in pyramid[i].split()]
#It will be easier to reverse the pyramid and start from the second row all the way down

n = len(pyramid)-1
reversepyramid = [pyramid[n-i] for i in range(n+1)]

for row in range(len(reversepyramid)):
    if row==0:
        continue
    else:
        for col in range(len(reversepyramid[row])):
            reversepyramid[row][col] += max([reversepyramid[row-1][col],reversepyramid[row-1][col+1]])

print(reversepyramid[-1][0])