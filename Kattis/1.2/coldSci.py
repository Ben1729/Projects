num = input()
temp = raw_input().split()

i = 0

for x in range(num):
    if  int(temp[x])< 0:
        i += 1
print i