s = str(input())

a = 0
b = 0
c = 0
d = 0
length = float(len(s))


for x in s:
    if x.islower():
        b += 1
    elif '_' == x:
        a += 1
    elif x.isupper():
        c += 1
    else:
        d += 1
a = a / length
b = b / length
c = c / length
d = d / length

print("{:.15f}".format(a))
print("{:.15f}".format(b))
print("{:.15f}".format(c))
print("{:.15f}".format(d))
