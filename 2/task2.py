file = open("input.txt")
lines = file.readlines()

sum = 0

colorTypes = ["red", "green", "blue"]

for line in lines:
    games = line.split(":")[1].split(";")
    games = [game.strip() for game in games]

    redMin = 0
    greenMin = 0
    blueMin = 0

    colorMins = [0 for i in range(len(colorTypes))]

    for game in games:
        colors = game.split(",")
        colors = [color.strip() for color in colors]
        for color in colors:
            number = int(color.split(" ")[0])
            for colorType in colorTypes:
                if (
                    colorType in color
                    and number > colorMins[colorTypes.index(colorType)]
                ):
                    colorMins[colorTypes.index(colorType)] = number

    power = 1
    for colorMin in colorMins:
        power *= colorMin
    sum += power

print(sum)
