def days(statues):
    printer = 1
    days = 0
    while printer < statues:
        printer = printer*2
        days+= 1
    days+=1
    return days

print days(int(raw_input()))