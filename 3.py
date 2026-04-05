from aoc_useful_functions import find_ints, all_occ, find

file = r"c:\Users\jledg\Documents\not_backed_up\input3.txt"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

def remove_negs(l, m1, m2):
    '''remove negative or overflowing coordinates from list of coordinates

    Parameters
    ----------
    l : _list_
        list of coordinates to filter
    m1 : _int_
        maximum 0th coordinate value (usually #rows - 1)
    m2 : _int_
        maximum 1st coordinate value (usually #cols - 1)

    Returns
    -------
    new_l : _list_
        filtered list
    '''
    new_l = [(el[0], el[1]) for el in l if (el[0]>= 0 and el[1]>= 0 and el[0]<= m1 and el[1] <= m2)]
    return new_l

def check_symb(lc, gears):
    '''check if `lc` is any symbol other than `.` (gears == False), or is an asterisk (gears == True)

    Parameters
    ----------
    lc : _Any_
        character to check
    gears : _bool_
        True if checking just for *, False otherwise

    Returns
    -------
    _bool_
        True if `lc` meets criterion, False otherwise
    '''
    if gears:
        if lc == "*": # if its a potential gear
            return True
        return False
                
    else:
        if lc != "." and lc != "\n": # if line[c] is a genuine symbol
            return True
        return False


def mark_coords(lines, gears):
    '''find all coordinates which touch a symbol (or specifically a gear, if gears == True)

    Parameters
    ----------
    lines : _list_
        grid (list of lists) to check
    gears : _bool_
        True if looking just for asterisks, False if looking for all symbols

    Returns
    -------
    touching : _list_
        list of all coordinates touching a symbol / gear
    '''
    line_no = -1
    touching = []

    for line in lines:
        line_no += 1
        for c in range(len(line)):
            # check if you've got an integer
            try:
                i = int(line[c])
            except ValueError:
                if check_symb(line[c], gears):
                    touching += [(line_no - k, c - j) for j in [-1, 0, 1] for k in [-1, 0, 1]]

    # remove negative values and duplicates, then sort
    touching = sorted(list(set(remove_negs(touching, len(lines)-1, len(lines[0])-2)))) 

    return touching

def part1():

    touching = mark_coords(lines, False)

    line_no = -1
    count = 0

    for line in lines:
        line_no += 1

        # find all integers
        ints = find_ints(line)
        bs = []
        c = 0

        for i in ints:
            if c == 0:
                # no ambiguity as to index
                bs.append(line.index(str(i)))
            else:
                # possibly the integer occurs twice, so chop off part of the line
                b = bs[c-1]
                e = b + len(str(ints[c-1]))
                bs.append(line[e:].index(str(i))+e)
            
            b = bs[-1]
            e = b + len(str(i))
            # all coords which contain part of the integer
            covered_coords = [(line_no, b + j) for j in range(e-b)]
            
            # if any part of the integer touches a symbol
            if set(covered_coords).intersection(set(touching)) != set([]):
                count += int(i)

            c += 1

    return count

def part2():
    # find all potential gears (asterisks)
    occs = find("*", lines)

    line_no = -1
    # gear dict keeps track of which integers touch each gear
    gear_dict = {}
    for g in occs:
        gear_dict[g] = []

    val = 0

    for line in lines:
        line_no += 1

        ints = find_ints(line)
        bs = []
        c = 0
        
        for i in ints:
            if c == 0:
                bs.append(line.index(str(i)))
            else:
                b = bs[c-1]
                e = b + len(str(ints[c-1]))
                bs.append(line[e:].index(str(i))+e)
            
            b = bs[-1]
            e = b + len(str(i))
            covered_coords = [(line_no, b + j) for j in range(e-b)]
            surroundings = []
            for coord in covered_coords:
                surroundings += [(coord[0]+j, coord[1]+k) for j in [-1, 0, 1] for k in [-1, 0, 1]]

            surroundings = sorted(list(set(remove_negs(surroundings, len(lines)-1, len(lines[0])-2))))
            inter = list(set(surroundings).intersection(set(occs)))

            if inter != []:
                for gear in inter:
                    # add integer to the list of integers this gear touches
                    old_val = gear_dict[gear]
                    new_val = old_val + [i]
                    gear_dict[gear] = new_val

            c += 1

    for gear in occs:
        g = gear_dict[gear]
        if len(g) == 2:
            # its a gear
            val += (g[0]*g[1])

    return val

#print(part2())