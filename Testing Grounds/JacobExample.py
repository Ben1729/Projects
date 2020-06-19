import string

letters = string.ascii_lowercase

n, m = input().split()

key = str(input())
msg = str(input())

output = []

for i in range(len(msg))

    if i < en(key):
        
        ki = key[i]
        mi = msg[i]
    
    else: 
        ki = msg[i]
        mi = msg[i]

    output.append(letters[(letters.index(ki) + letters.index(mi)) % 26])

    print "".join(output)
