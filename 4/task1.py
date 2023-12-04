import math

file = open("input.txt")
lines = file.readlines()

sum = 0

for line in lines:
    values = line.split(":")[1].strip().split("|")
    input = values[0].strip().split(" ")
    winning = values[1].strip().split(" ")
    matches = 0
    for num in input:
        if num.isdigit() and num in winning:
            matches += 1

    sum += math.pow(2, matches - 1) if matches > 0 else 0

print(int(sum))
