f = open("file.txt", "r")

lstitem = ['o', 't', 'f', 's', 'e', 'n']
lst = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
newlst = []

def check(sentence, nindex):
    str = sentence[nindex:nindex+5]
    filtered = {key: value for key, value in lst.items() if key.startswith(str[0])}
    for k in filtered:
        if str.startswith(k):
            newlst.append(lst[k])
            return len(k)-1
    return 1

def numeric(sentence):
    i = 0
    while (i < len(sentence)):
        if sentence[i].isdigit():
            # print(sentence[i])
            newlst.append(int(sentence[i]))
            i+=1
        elif sentence[i] in lstitem:
            # print(sentence[i])
            x = check(sentence, i)
            i+=x
        elif sentence[i:i+2] == "\n":
            i+=1
        else:
            i+=1


sum = 0

for line in f:
    # getAlNumeric(line)
    numeric(line.strip())
    print(newlst)
    first = newlst[0]
    last = newlst[-1]
    num = str(first)+str(last)
    sum += int(num)
    # print(num)
    newlst.clear()

print(sum)


f.close()
