# future proof
# handle large integer time stamps

# keep a list of tuples
# meeting list (2, 3)

meetingTupleList = [(2, 3), (8, 9), (2, 5), (0, 3), (3, 4), (10, 20), (11, 30), (-100, 0)]

def CondenseMeetingTimes(meetingTupleList):
    if len(meetingTupleList) == 0 :
        print "no meetings today"
        return
        
    meetingTupleList = sorted(meetingTupleList)
    print meetingTupleList
        
    condenseTupleList = [list(meetingTupleList[0])]
    for index, timeTuple in enumerate(meetingTupleList) :
    	for condenseTimeTuple in condenseTupleList :
            if timeTuple[1] < condenseTimeTuple[0] :
                # insert in front of condenseTimeTuple
                condenseTupleList.insert(index, list(timeTuple))
                break
            elif timeTuple[0] > condenseTimeTuple[1] :
                # move onto next condenseTimeTuple
                if condenseTimeTuple == condenseTupleList[-1] :
                    # at the end of the condense list, append here
                    condenseTupleList.append(list(timeTuple))
                continue
            
            # if arrives here, there is a shared subset between the two tuples
            # timeTuple[1] > condenseTimeTuple[0]
            # and timeTuple[0] < condenseTimeTuple[1]
            if timeTuple[0] < condenseTimeTuple[0] :
            	condenseTimeTuple[0] = timeTuple[0]
                break
                
            if timeTuple[1] > condenseTimeTuple[1] :
                condenseTimeTuple[1] = timeTuple[1]
                break
                
            if timeTuple[0] >= condenseTimeTuple[0] and timeTuple[1] < condenseTimeTuple[1] :
                break
	
    print condenseTupleList[:]

print "result:"
CondenseMeetingTimes(meetingTupleList)