file = open("input.txt")
lines = file.readlines()

redLimit = 12
greenLimit = 13
blueLimit = 14

sumIds = 0

for line in lines:
    gameId = line.split(":")[0].split(" ")[1]
    games = line.split(":")[1].split(";")
    games = [game.strip() for game in games]
    possible = True
    for game in games:
        colors = game.split(",")
        colors = [color.strip() for color in colors]
        for color in colors:
            number = int(color.split(" ")[0])
            if "red" in color and number > redLimit:
                possible = False
            elif "green" in color and number > greenLimit:
                possible = False
            elif "blue" in color and number > blueLimit:
                possible = False
    if possible:
        sumIds += int(gameId)

print(sumIds)
