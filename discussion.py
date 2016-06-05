"""Rescursion"""

# Is a function that calls itself.
# It is important to have a base case because it helps a recursive function to stop if a condition has been violated.

"""Graphs"""

# Graphs are like trees, but they can contain loops, and not necesarily have a root. The relationship between the nodes can be directed or non-directed.

# See previous answer.

# Driving route planner.
"""Performance of Different Data Structure"""

''' Data Structure         Index   Search  Add-R   Add-L   Pop-L   Pop-R'''
#   Python List Array      o(1)     o(n)   o(1)    o(n)     o(n)     o(1)
#   Linked List            o(n)     o(n)   o(1)    o(1)     o(1)     o(n)
#   Doubly-Linked List     o(n)     o(n)   o(1)    o(1)     o(1)     o(1)
#   Queue as Array         -         -     o(1)    -        o(n)     -
#   Queue as LL or DLL     -         -     o(1)    -        o(1)     -
#   Stack as Array, LL, DLL -        -     o(1)    -        -        o(1)
#   Deque as DLL            -        -     o(1)    o(1)     o(1)     o(1)

'''Data Structure       Get     Add     Delete  Iterate Memory'''
# Dictionary (Hash Map)   O(1)    O(1)    O(1)    O(n)    medium
# Set (Hash Map)          O(1)    O(1)    O(1)    O(n)    medium
# Binary Search Tree     O(log n) O(n)    O(n)    O(1)    low
# Tree                    O(n)    O(1)    O(1)    O(n)    low


"""Sorting"""
# Bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Runtime is o(n^2)

# Merge Sort takes two sorted lists and creates a new list that is in order. First, it compares the first element of each sorted list. Remove whichever element that is lower and appends it to the new list. It will continue comparing the elements until the list are empty. Runtime is o(nlog(n)).

# Quick Sort operates in place. The list will have a pivot. Then using the pivot as reference, we can move all the numbers lower than the pivot number to the beginning of the list and move all the numbers bigger than the pivot to the right of the pivot number.

"""Git Branching"""

# To test new implementations safely and maintain separate releases.
# Pull requests are used to tell others about the changes that have been pushed to the Github repository. Once a pull request is sent, interested parties can review the changes, have a discussion about the code, or merge them to the master branch.
