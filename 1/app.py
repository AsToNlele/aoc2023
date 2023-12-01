file = open("input.txt")
lines = file.readlines()

letterNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0


class Number:
    def __init__(self, index, number):
        self.index = index
        self.number = number

    def __str__(self):
        return f"Number(index={self.index}, number={self.number})"

    def __repr__(self):
        return f"Number(index={self.index}, number={self.number})"


for line in lines:
    firstDigit = Number(-1, -1)
    lastDigit = Number(-1, -1)

    numbers = []

    # Find all letter numbers
    # Uncomment for part 2
    # for i in range(len(line)):
    #     for letterNumber in letterNumbers:
    #         if line.startswith(letterNumber, i):
    #             numbers.append(Number(i, letterNumbers.index(letterNumber) + 1))

    # Find all digit numbers
    for i, number in enumerate(line):
        if number.isdigit():
            numbers.append(Number(i, int(number)))

    # Find first and last digit
    for number in numbers:
        if number.index < firstDigit.index or firstDigit.index == -1:
            firstDigit = number
        if number.index > lastDigit.index or lastDigit.index == -1:
            lastDigit = number

    sum += int(f"{firstDigit.number}{lastDigit.number}")

print(sum)
