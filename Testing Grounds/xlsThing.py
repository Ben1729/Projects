from openpyxl import load_workbook

workbook = load_workbook(filename="coding1.xlsx")
sheet = workbook.active

result = ""
fResult = ""
for x in range(1,200):
    if x % 3 == 0:
        result = result + sheet[("A"+str(x))].value[1]
    elif x % 2 == 0:
        result = result + sheet[("A"+str(x))].value[2]
i = 0
for char in result:
    i += 1
    if i % 5 == 0:
        fResult = fResult + char
print(fResult)
