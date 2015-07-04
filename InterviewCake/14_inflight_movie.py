flight_length = 200
movie_length = [30, 100, 50, 70, 90, 40, 30, 100, 100, 110, 150]

# returns boolean indicating whether there are two numbers in movie_length
# whose sums equals flight_length

# Optimize for runtime over memory

# SOLUTION 1
# use a dictionary to record 2 movie length sums
# with each new flight time, ask the dictionary if there is a match

def TwoMoviesLenSum(movieLenList):
    twoMoviesLenDict = {}
    for firstMovieLen in movieLenList:
        for secondMovieLen in movieLenList[movieLenList.index(firstMovieLen):]:
            lenKey = firstMovieLen + secondMovieLen
            if lenKey in twoMoviesLenDict:
            	twoMoviesLenDict[lenKey] += 1
            else:
                twoMoviesLenDict[lenKey] = 1
            
    return twoMoviesLenDict
        	

def TwoMovieLenEqualToFlightLen(flightLen, twoMoviesLenDict):
    if flightLen in twoMoviesLenDict:
        return True
    else:
        return False
    
    
twoMoviesLenDict = TwoMoviesLenSum(movie_length)
print twoMoviesLenDict

print TwoMovieLenEqualToFlightLen(flight_length, twoMoviesLenDict)

# SOLUTION 2
# use dictionary 

def MovieFlightMatch(flightLen, movieLenList):
    movieLenDict = {}
    for movieIndex, movieLen in enumerate(movieLenList):
        # check to see if there is a match before putting this movie in the dictionary
        # because this movie is not in the dictionary yet, we can't watch the same movie twice
        searchMovieLen = flightLen - movieLen
        if searchMovieLen in movieLenDict:
            return True
        
        if movieLen in movieLenDict:
        	movieLenDict[movieLen].append(movieIndex)
        else:
            movieLenDict[movieLen] = [movieIndex]
    
    return False

print MovieFlightMatch(flight_length, movie_length)
   		












