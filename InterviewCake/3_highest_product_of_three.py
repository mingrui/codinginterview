# special cases:
# 0 is one of the 3 numbers
# even number of negative numbers
# can't simply find the highest 3 numbers
# 2 negative numbers product can be higher than 2 positive numbers

# find highest 3 positive numbers, including 0
# find lowest 2 negative numbers, take the product
# if lower 2 of 3 positive numbers' product is lower than the negative numbers' product
# 	then use the 1 highest positive number and the 2 negative numbers 
# else
# 	use the highest 3 positive numbers

listOfInts = [1, 2, 3, 4, -4, -8, 5, -1, -9]

def highestProductOfThree(listOfInts):
    
    highestThreePositive = [0, 0, 0]
    lowestTwoNegative = [0, 0]
    
    for item in listOfInts:
    	if item >= 0 :
            # put into highestThreePositive list
            if item > highestThreePositive[0] :
                highestThreePositive[2] = highestThreePositive[1]
                highestThreePositive[1] = highestThreePositive[0]
                highestThreePositive[0] = item
            elif item > highestThreePositive[1] :
                highestThreePositive[2] = highestThreePositive[1]
                highestThreePositive[1] = item
            elif item > highestThreePositive[2] :
                highestThreePositive[2] = item
        else:
            # put into lowestTwoNegative list
            if item < lowestTwoNegative[1] :
                lowestTwoNegative[0] = lowestTwoNegative[1]
                lowestTwoNegative[1] = item
            elif item < lowestTwoNegative[0] :
                lowestTwoNegative[0] = item
                
	print highestThreePositive[0]
    print highestThreePositive[1]
    print highestThreePositive[2]
    
    print lowestTwoNegative[0]
    print lowestTwoNegative[1]
    
    productOfTwoNegative = lowestTwoNegative[0] * lowestTwoNegative[1]
    productOfLowerTwoPositive = highestThreePositive[1] * highestThreePositive[2]
    print productOfTwoNegative
    print productOfLowerTwoPositive
    
    maxProduct = 0
    if productOfTwoNegative > productOfLowerTwoPositive :
        maxProduct = productOfTwoNegative * highestThreePositive[0]
    else :
    	maxProduct = productOfLowerTwoPositive * highestThreePositive[0]
        
    print maxProduct
    
highestProductOfThree(listOfInts)
    