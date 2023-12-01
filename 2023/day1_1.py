import re
f = open("file.txt", "r")

# lst = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getNumeric(sentence):
    numeric_values = re.findall(r'\d', sentence)

    if numeric_values:
        first_numeric = int(numeric_values[0])
        last_numeric = int(numeric_values[-1])
        return first_numeric, last_numeric
    else:
        return None, None

sum = 0

for line in f:
    first, last =  getNumeric(line)
    num = str(first)+str(last)
    sum += int(num)

print(sum)

f.close()
