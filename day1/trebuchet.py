
numbers = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "thre3e",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "sev7en",
    "eight": "ei8ght",
    "nine": "ni9ne"
}
f = open("input", "r")
count = 0
for line in f.readlines():
    for word, number in numbers.items():
        line = line.replace(word, number)
    line = ''.join([str(i) for i in line if i.isdigit()])
    
    if len(line) == 1:
        line = line * 2
    elif len(line) > 2:
        line = line[::len(line)-1]
    print(line)
    count += int(line)
print(count)