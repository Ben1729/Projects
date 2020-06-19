s = str(raw_input())
print ''.join(x for x in s if (not x.islower()) and (not "-" in x))