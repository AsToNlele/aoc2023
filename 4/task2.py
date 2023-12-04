file = open("input.txt")
lines = file.readlines()

sum = 0


def checkLine(cardNumber):
    global sum
    sum += 1
    values = lines[cardNumber - 1].split(":")[1].strip().split("|")
    input = values[0].strip().split(" ")
    winning = values[1].strip().split(" ")
    matches = 0
    for num in input:
        if num.isdigit() and num in winning:
            matches += 1

    if matches > 0:
        arr = list(range(cardNumber + 1, cardNumber + matches + 1))
        for i in arr:
            checkLine(i)


for index, line in enumerate(lines):
    checkLine(index + 1)

print(sum)
