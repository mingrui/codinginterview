# binary search
words = [
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'xiaosaurus',
    'xiphias',
    'xylophone',
]

def BinarySearchForRotationPoint(words):
    firstWord = words[0]
    floorIndex = 0
    ceilingIndex = len(words) - 1
    while(floorIndex < ceilingIndex):
        guessIndex = floorIndex + (ceilingIndex - floorIndex) / 2
        if words[guessIndex] < firstWord:
            ceilingIndex = guessIndex
        else:
            floorIndex = guessIndex
            
        if floorIndex + 1 == ceilingIndex:
            if ceilingIndex == len(words) - 1: # Bonus, search always seeks backwar
                return 0
            return ceilingIndex
    
print words[BinarySearchForRotationPoint(words)]