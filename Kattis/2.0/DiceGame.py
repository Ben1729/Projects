gunnerDie = input().split()
emmaDie = input().split()

gunnerTot = 0
emmaTot = 0
for x in gunnerDie:
    gunnerTot += int(x)
for x in emmaDie:
    emmaTot += int(x)

if gunnerTot > emmaTot:
    print("Gunnar")
elif emmaTot > gunnerTot:
    print("Emma")
else:
    print("Tie")