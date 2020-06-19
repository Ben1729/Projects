for x in range(int(input())-1):
    name, startDate, born, cources = input().split()
    if int(startDate.split("/")[0]) >= 2010:
        if int(born.split("/")[0]) >= 1993:
            if int(cources) >= 8:
                print(name + " eligible")
            else:
                print(name + " ineligible")
        else:
            print(name + " ineligible")
    else:
        print(name + " ineligible")

name, startDate, born, cources = input().split()

print(name +" coach petitions")