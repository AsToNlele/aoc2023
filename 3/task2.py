file = open("input.txt")
lines = file.readlines()


class Number:
    def __init__(self, x: int, y: int, value: int):
        self.xFrom = x
        self.xTo = x + len(str(value)) - 1
        self.y = y
        self.value = value
        self.hasGear = False

    def __str__(self):
        return f"Number({self.xFrom}, {self.xTo}, {self.y}, {self.value}, {self.hasSymbol})"

    def __repr__(self):
        return self.__str__()


arr = [list(line.strip()) for line in lines]

numbers = []


class Gear:
    def __init__(self, x: int, y: int, number: int):
        self.x = x
        self.y = y
        self.number = number

    def __str__(self):
        return f"Gear({self.x}, {self.y}, {self.number})"

    def __repr__(self):
        return self.__str__()


def findNumbers(arr):
    numbers = []
    currentNumber = None
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].isdigit():
                if currentNumber is None:
                    currentNumber = Number(j, i, int(arr[i][j]))
                else:
                    currentNumber = Number(
                        currentNumber.xFrom,
                        currentNumber.y,
                        currentNumber.value * 10 + int(arr[i][j]),
                    )
            else:
                if currentNumber is not None:
                    numbers.append(currentNumber)
                    currentNumber = None

    return numbers


def checkSurroundings(arr: list[list[str]], number: Number):
    xes = list(range(number.xFrom, number.xTo + 1))
    y = number.y
    arrMaxX = len(arr[0]) - 1
    arrMaxY = len(arr) - 1
    gear = Gear(-1, -1, -1)
    hasGear = False

    # Check top
    if y > 0:
        # Check top middle
        for x in xes:
            if arr[y - 1][x] == "*":
                hasGear = True
                gear = Gear(x, y - 1, number.value)
                break
        # Check top left diagonal
        if xes[0] > 0 and (arr[y - 1][xes[0] - 1] == "*"):
            hasGear = True
            gear = Gear(xes[0] - 1, y - 1, number.value)

        # Check top right diagonal
        if xes[-1] < arrMaxX and (arr[y - 1][xes[-1] + 1] == "*"):
            hasGear = True
            gear = Gear(xes[-1] + 1, y - 1, number.value)

    # Check left
    if xes[0] > 0 and (arr[y][xes[0] - 1] == "*"):
        hasGear = True
        gear = Gear(xes[0] - 1, y, number.value)

    # Check right
    if xes[-1] < arrMaxX and (arr[y][xes[-1] + 1] == "*"):
        hasGear = True
        gear = Gear(xes[-1] + 1, y, number.value)

    # Check bottom
    if y < arrMaxY:
        # Check bottom middle
        for x in xes:
            if arr[y + 1][x] == "*":
                hasGear = True
                gear = Gear(x, y + 1, number.value)
                break
        # Check bottom left diagonal
        if xes[0] > 0 and (arr[y + 1][xes[0] - 1] == "*"):
            hasGear = True
            gear = Gear(xes[0] - 1, y + 1, number.value)

        # Check bottom right diagonal
        if xes[-1] < arrMaxX and (arr[y + 1][xes[-1] + 1] == "*"):
            hasGear = True
            gear = Gear(xes[-1] + 1, y + 1, number.value)

    return gear if hasGear else None


numbers = findNumbers(arr)
gears = []
gearRatioSum = 0

# Chech gears around numbers
for number in numbers:
    res = checkSurroundings(arr, number)
    if res is not None:
        gears.append(res)

# Check for duplicate gears
for i, _ in enumerate(gears):
    for j, _ in enumerate(gears):
        if i == j:
            continue
        if gears[i].x == gears[j].x and gears[i].y == gears[j].y:
            gearRatioSum += gears[i].number * gears[j].number
            break

gearRatioSum /= 2

print(int(gearRatioSum))
