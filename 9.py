#pythagorean triplet
#facts: 0<a<b<c<999, a = 1000-b-c. The simplest way to do this will be to check all combinations of b and c, which will be less 999**2, due to iterating b from 1 to c for every c.
found=False

for c in range(1,1000):
    for b in range(1,c):
        a = 1000 - b - c
        if a**2+b**2==c**2:
            print(a,b,c,a*b*c)
            found = True
            break
    if found == True:
        break
