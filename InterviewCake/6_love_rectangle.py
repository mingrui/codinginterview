rectOne = {
	'x' : 1,
    'y' : 5,
    'width' : 10,
    'height' : 4,
}

rectTwo = {
	'x' : -1,
    'y' : 7,
    'width' : 10,
    'height' : 10
}

def xOverlap(x1, width1, x2, width2):
    highestStartPoint = max(x1, x2)
    lowestEndPoint = min(x1 + width1, x2 + width2)
    if highestStartPoint >= lowestEndPoint :
        return (None, None)
    overlapWidth = lowestEndPoint - highestStartPoint
    return (highestStartPoint, overlapWidth)

def FindRangeOverlap(start1, end1, start2, end2):
    highestStartPoint = max(start1, start2)
    lowestEndPoint = min(start1 + end1, start2 + end2)
    if highestStartPoint >= lowestEndPoint :
        return (None, None)
    overlapLength = lowestEndPoint - highestStartPoint
    return (highestStartPoint, overlapLength)
            
print FindRangeOverlap(rectOne['x'], rectOne['width'], rectTwo['x'], rectTwo['width'])
print FindRangeOverlap(rectOne['y'], rectOne['height'], rectTwo['y'], rectTwo['height'])