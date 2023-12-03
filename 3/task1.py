file = open("input.txt")
lines = file.readlines()

sum = 0


class Number:
    def __init__(self, x: int, y: int, value: int):
        self.xFrom = x
        self.xTo = x + len(str(value)) - 1
        self.y = y
        self.value = value
        self.hasSymbol = False

    def __str__(self):
        return f"Number({self.xFrom}, {self.xTo}, {self.y}, {self.value}, {self.hasSymbol})"

    def __repr__(self):
        return self.__str__()


arr = [list(line.strip()) for line in lines]

numbers = []


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
    hasSymbol = False

    # Check top
    if y > 0:
        # Check top middle
        for x in xes:
            if arr[y - 1][x] != "." and arr[y - 1][x].isdigit() is False:
                hasSymbol = True
                break
        # Check top left diagonal
        if xes[0] > 0 and (
            arr[y - 1][xes[0] - 1] != "." and arr[y - 1][xes[0] - 1].isdigit() is False
        ):
            hasSymbol = True

        # Check top right diagonal
        if xes[-1] < arrMaxX and (
            arr[y - 1][xes[-1] + 1] != "."
            and arr[y - 1][xes[-1] + 1].isdigit() is False
        ):
            hasSymbol = True

    # Check left
    if xes[0] > 0 and (
        arr[y][xes[0] - 1] != "." and arr[y][xes[0] - 1].isdigit() is False
    ):
        hasSymbol = True

    # Check right
    if xes[-1] < arrMaxX and (
        arr[y][xes[-1] + 1] != "." and arr[y][xes[-1] + 1].isdigit() is False
    ):
        hasSymbol = True

    # Check bottom
    if y < arrMaxY:
        # Check bottom middle
        for x in xes:
            if arr[y + 1][x] != "." and arr[y + 1][x].isdigit() is False:
                hasSymbol = True
                break
        # Check bottom left diagonal
        if xes[0] > 0 and (
            arr[y + 1][xes[0] - 1] != "." and arr[y + 1][xes[0] - 1].isdigit() is False
        ):
            hasSymbol = True

        # Check bottom right diagonal
        if xes[-1] < arrMaxX and (
            arr[y + 1][xes[-1] + 1] != "."
            and arr[y + 1][xes[-1] + 1].isdigit() is False
        ):
            hasSymbol = True

    return hasSymbol


numbers = findNumbers(arr)
for number in numbers:
    if checkSurroundings(arr, number):
        sum += number.value
print(sum)
