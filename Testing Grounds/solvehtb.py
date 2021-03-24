authArr = []

with open('auth.json', 'r') as cmpfile:
    t = cmpfile.readlines()
    for x in t:
        if '"' in x:
            authArr.append(x.split('"')[1])

with open('syslog','r' ) as infile:
    for x in infile.readlines():
        if 'SerialNumber' in x and 'SerialNumber=3' not in x:
            if x.split('SerialNumber: ')[1].replace('\n','') not in authArr:
                print(x)
