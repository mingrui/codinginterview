"""
Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly "first come,
first out" basis. People must adopt either the "oldest" (based on arrivale time) of all 
animals at the shelter, or they ccan select whether they would prefer a dog or a cat
(and will receive the oldest animal of that type). They cannot select which sepcific
animal they would like. Create the data structures to maintain this system and implement
operations such as enqueue, dequeueAny, dequeueDog, dequeueCat. You may use the built-in
LinkedList data structure
"""

"""
Keep 2 lists for cat and dog, store timestamp with each entry
"""