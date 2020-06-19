cases = int(input())
items = []
for x in range(cases):
    items.append(str(input()))
alpha = sorted(items)
revAlpha = alpha.copy()
revAlpha.reverse()
if items == alpha:
    print("INCREASING")
elif items == revAlpha:
    print("DECREASING")
else:
    print("NEITHER")