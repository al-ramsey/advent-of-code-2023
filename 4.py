file = r"c:\Users\jledg\Documents\not_backed_up\input4.txt"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

lines = [line[8:-1] for line in lines]
lines = [line.split(" | ") for line in lines]
lines = [[l.split(" ") for l in line] for line in lines]
lines = [[[x for x in y if x != ""] for y in z] for z in lines]

def part1():

    s = 0

    for line in lines:
        winning_nos = list(set(line[0]).intersection(set(line[1])))
        # 2^{-1} = 1/2 :(
        if winning_nos == []:
            continue
        else:
            s += 2**(len(winning_nos) - 1)

    return s

#print(part1())

def part2():

    card_count = 0
    # create a dictionary to keep track of how many of each card we have
    card_dict = {}
    # start with one each
    for i in range(len(lines)):
        card_dict[i+1] = 1

    count = 1
    for line in lines:
        winning_nos = list(set(line[0]).intersection(set(line[1])))
        n = len(winning_nos)
        for j in range(1, n+1):
            # win one for each copy of the current card we have
            card_dict[count + j] += card_dict[count]

        count += 1
        
    # sum them all up
    for i in range(1, len(lines)+1):
        card_count += card_dict[i]

    return card_count

#print(part2())