"""
Missing int

Given an input file with four billion non-negative integers, provide an 
algorithm to generate an integer that is not contained in the file.
Assume you have 1 GB of memory available for this task.

FOLLOW UP
What if you have only 10 MB of memory? Assume that all the values 
are distinct and we now have no more than one billion non-negative
integers
"""

from bitarray import bitarray

# Hard Problem
a = bitarray(600000)
# Bit vector
a[599999] = 1
print a