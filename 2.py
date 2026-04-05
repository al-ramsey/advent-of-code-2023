file = r"c:\Users\jledg\Documents\not_backed_up\aoc_2-input.txt"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

def part1(only):
    count = 0
    for line in lines:
        blue = []
        red = []
        green = []
        rounds = line.split(": ")[-1]
        num = int((line.split(": ")[0])[5:])
        rounds = rounds.split("; ")
        for round in rounds:
            round = round.split(", ")
            for r in round:
                if "blue" in r:
                    blue.append(int(r[:-5]))
                elif "red" in r:
                    red.append(int(r[:-4]))
                else:
                    green.append(int(r[:-6]))
        
        good = True 

        if max(red) > only[0] or max(green) > only[1] or max(blue) > only[2]:
                good = False
        
        if good:
            count += num

    return count

print(part1([12, 13, 14]))

def part2():
    count = 0
    for line in lines:
        blue = []
        red = []
        green = []
        rounds = line.split(": ")[-1]
        num = int((line.split(": ")[0])[5:])
        rounds = rounds.split("; ")
        for round in rounds:
            round = round.split(", ")
            for r in round:
                if "blue" in r:
                    blue.append(int(r[:-5]))
                elif "red" in r:
                    red.append(int(r[:-4]))
                else:
                    green.append(int(r[:-6]))
        #print(red)
        #print(green)
        #print(blue)

        if blue == []:
            blue = [0]
        if red == []:
            red = [0]
        if green == []:
            green == [0]
        
        power = max(blue)*max(red)*max(green)
        #print(power)
        count += power

    return count

print(part2())