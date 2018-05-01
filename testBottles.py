from bottles import line
from bottles import song
from bottles import main

result = '72 bottles of beer on the wall, 72 bottles of beer, take one down, pass it around, 71 bottles of beer on the wall'
assert line(72) == result, "Should print out line of song"

numOfLines = 99
assert len(song(numOfLines)) == numOfLines, 'Should have correct number of lines'