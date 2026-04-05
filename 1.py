file = r"c:\Users\jledg\Documents\not_backed_up\input1.txt"
filein = open(file, "r", encoding='UTF-8')
lines = filein.readlines()
filein.close()

def first_digit(l):
    '''find first digit appearing in a string l

    Parameters
    ----------
    l : _str_
        string to analyse

    Returns
    -------
    i : _int_
        first digit appearing in l
    '''
    found = False
    for el in l:
        try:
            i = int(el)
            found = True
            break
        except ValueError:
            continue

    if found:
        return i
    else:
        return -1

def part1():

    s = 0

    for line in lines:
        i = str(first_digit(line))
        j = str(first_digit(reversed(line)))
        s += int(i+j)

    return s

#print(part1())

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def finder(l, digits):
    '''find first `extended digit` appearing in the string l

    Parameters
    ----------
    l : _str_
        string to analyse
    digits : _list_
        list of `word digits` to look out for

    Returns
    -------
    i : _str_
        first extended digit appearing in l (integer, if originally word digit, e.g. one -> 1 -> '1')
    '''
    i = str(first_digit(l))
    if int(i) >= 0:
        ind = l.index(i)
    else:
        ind = len(l) + 1

    dig_indices = []
    for d in digits:
        if d in l:
            dig_indices.append(l.index(d))
        else:
            dig_indices.append(len(l))
    
    if min(dig_indices) < ind:
        i = str(dig_indices.index(min(dig_indices)) + 1)

    return i

def part2():

    s = 0
    for line in lines:
        i = finder(line, digits)
        j = finder("".join(line[::-1]), ["".join(d[::-1]) for d in digits])
        s += int(i+j)
        
    return s

print(part2())
