import fileinput

first = True
images = []

for line in fileinput.input():
    if line[0] not in ['#', '.']:
        images.append([])

    to_print = line[0]
    line = line[2:]

    images[-1].append("")
    for i in line.split():
        i = int(i)
        for j in range(i):
            images[-1][-1] = images[-1][-1] + to_print
        if to_print == '#':
            to_print = '.'
        else:
            to_print = '#'


first = True
for i in images[:-1]:
    if first:
        first = False
    else:
        print()

    i = i[1:]

    for j in i:
        print(j)

    works = True
    for j in range(0, len(i)-1):
        if len(i[j]) != len(i[j+1]):
            works = False

    if not works:
        print("Error decoding image")