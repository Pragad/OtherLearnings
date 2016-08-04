"""
Merge function for 2048 game.
"""

"""
The following function creates a list of the given sized
and fill it with Zeros
Input: Size of the list
Output: A list filled with Zeros.
"""
def zeroListMaker(n):
    listofzeros = [0] * n
    return listofzeros

"""
The following function copies non-zero elements from one 
list to another. 
Input: Two lists, one destination and another source
Note that the destination list in this case is an empty
list filled with Zeros.
"""
def moveZeroToEnd(res, lin):
    res_index = 0
    
    for item in lin:
        if (item != 0):
            res[res_index] = item
            res_index += 1
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = zeroListMaker(len(line))
    moveZeroToEnd(result, line)
    
    print '\n'
    print result
    index2 = 0
    for item in result:
        if (item == 0):
            index2 += 1
            continue
        
        if (index2+1 < len(result)): 
            if (item == result[index2 + 1]):
                result[index2] = item*2
                result[index2 + 1] = 0
            index2 += 1
    
    final_result = zeroListMaker(len(result))
    moveZeroToEnd(final_result, result)
    return final_result
#    return []

list1 = [2, 0, 2, 4]
print merge(list1)


list2 = [0, 0, 2, 2]
print merge(list2)

list3 = [2, 2, 0, 0]
print merge(list3)

list4 = [2, 2, 2, 2, 2]
print merge(list4)

list5 = [8, 16, 16, 8]
print merge(list5)

list6 = [2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]
print merge(list6)

list7 = [2, 0, 0, 2, 0, 0, 0, 2, 0, 4, 0, 2]
print merge(list7)

list8 = [2, 0, 0, 2, 0, 0, 0, 2, 0, 4, 4, 2]
print merge(list8)

