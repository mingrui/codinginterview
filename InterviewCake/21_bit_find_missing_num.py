# many duplicate integers and one unique integer
# SOLUTION 1
# O(n) go through list linearly, put each integer into a dictionary

def FindLostNum(list_of_number):
    num_dict = {}
    for num in list_of_number:
        if num in num_dict:
            num_dict.pop(num)
        else:
            num_dict[num] = num
    return num_dict.itervalues().next()
    
list_of_drones = range(0, 100)
list_of_returning_drones = range(0, 100)
list_of_returning_drones.remove(88)
list_of_drones.extend(list_of_returning_drones)

print FindLostNum(list_of_drones)

# SOLUTION 2
def BitFindLostNum(list_of_ids):
    unique_id = 0
    
    for delivery_id in list_of_ids:
        unique_id ^= delivery_id
        
    return unique_id

print BitFindLostNum(list_of_drones)
    