target = input()
tries = str(input())
fails = 0
i = 0
failed = False
for x in tries:
    if failed == True:
        fails += 1
    failed = True
    for y in target:
        if x == y:
            failed = False
            i += 1
    if fails == 10 or i == len(target):
        break
if fails >= 10:
    print("LOSE")
else:
    print("WIN")