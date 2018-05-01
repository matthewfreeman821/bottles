

def line(numBottles):
    current = numBottles
    next = numBottles - 1

    if current > 1 or current == 0:
        firstPart = '%d bottles of beer on the wall, %d bottles of beer, take one down, pass it around, ' % (current, current)
    else:
        firstPart = '%d bottle of beer on the wall, %d bottle of beer, take one down, pass it around, ' % (current, current)
    
    if next > 1 or next == 0:
        secondPart = '%d bottles of beer on the wall' % (next)
    else:
        secondPart = '%d bottle of beer on the wall' % (next)

    return firstPart + secondPart

def song(numOfLines):
    linesOfSong = []
    for i in range(numOfLines, 0, -1):
        linesOfSong.append(line(i))
    
    return linesOfSong

def main ():
    print(song(99))

main()
