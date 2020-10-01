x = int(input())

factors = 0
factor = 2

while (factor*factor <= x):
    if (x % factor == 0):
        x /= factor
        factors += 1
    else:
        factor +=1
print(factors+1)