dictionary = {}
while(True):
    s = str(input()).split()
    if(not s):
        break
    else: 
        dictionary[s[1]] = s[0]
while(True):
    s = ""
    try:
        s = str(input())
    except:
        exit()
    translation = dictionary[s]
    if not translation:
        print("eh")
    else:
        print(translation)
