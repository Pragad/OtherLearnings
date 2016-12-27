"""
Merge function for 2048 game.
"""

def zero_list_maker(size):
    """
    The following function creates a list of the given sized
    and fill it with Zeros
    Input: Size of the list
    Output: A list filled with Zeros.
    """    
    listofzeros = [0] * size
    return listofzeros

def move_zero_to_end(res, lin):
    """
    The following function copies non-zero elements from one 
    list to another. 
    Input: Two lists, one destination and another source
    Note that the destination list in this case is an empty
    list filled with Zeros.
    """
    res_index = 0
    
    for item in lin:
        if (item != 0):
            res[res_index] = item
            res_index += 1
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    tmp_result = zero_list_maker(len(line))
    move_zero_to_end(tmp_result, line)
    
    index2 = 0
    for item in tmp_result:
        if (item == 0):
            index2 += 1
            continue
        
        if (index2+1 < len(tmp_result)): 
            if (item == tmp_result[index2 + 1]):
                tmp_result[index2] = item*2
                tmp_result[index2 + 1] = 0
            index2 += 1
    
    final_result = zero_list_maker(len(tmp_result))
    move_zero_to_end(final_result, tmp_result)
    return final_result