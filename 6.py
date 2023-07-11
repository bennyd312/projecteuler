#We know the formulas for finite partial sum of squares and finite partial sum of a series
n = 100

square_sum = n*(n+1)*(2*n+1)/6
series_sum = n*(n+1)/2
difference = series_sum**2-square_sum
print(difference)
