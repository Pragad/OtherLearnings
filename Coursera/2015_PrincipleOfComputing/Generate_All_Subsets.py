# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def gen_all_subsets(hand):
    """
    Iterative function that enumerates the set of all 
    subsets of outcomes.
    """
    print "\nHand: ", hand
    answer_set = set([()])
    for dummy_idx in range(len(hand)-1):
        print "1st For"
        temp_set = set([()])
        for partial_sequence in answer_set:
            print "2nd For"
            for item in hand:
                print "3rd For"
                new_sequence = list(partial_sequence)
                print "NS 1: ", new_sequence
                new_sequence.append(item)
                print "NS 2: ", new_sequence
                temp_set.add(tuple(sorted(new_sequence)))
                print "TS: ", temp_set
        #print temp_set
        #answer_set.append(temp_set)
        #answer_set = temp_set
        answer_set.update(temp_set)
        print "AS: ", answer_set
        print "\n"
    print "Ans Set: ", answer_set
    temp_set.add(hand)
    print "Temp_set: ", temp_set
    return temp_set

def gen_all_subsets_2(hand):
    print "\nHand: ", hand
    answer_set = set([()])
    
    temp_set = set([()])
    for dummy_x in range(len(hand)):
        temp_list = []
        
        for partial_temp_set in temp_set:
            for item in hand:
                print "Item: ", item
                temp_list.append(item)
                temp_set.add(tuple(temp_list))
                print "Temp Set: ", temp_set
    print answer_set
    
def get_string_length(string):
    """
    This function computes the length of a string.
    __len__() is not working in code skulptor
    """
    length = 0
    for dummy_x in string:
        length += 1
    return length
        
def gen_ones_set(number):
    """
    This function returns a list of indexes where '1' is
    set in a number
    """
    str_num = str(number)[::-1]
    
    ones_list = []
    for dummy_x in range(get_string_length(str_num)):
        if (str_num[dummy_x] == '1'):
            ones_list.append(dummy_x)
    
    return ones_list

def gen_all_subsets_bin(hand): 
    """
    This function generates all subsets by using Binary
    method. i.e. take items where 1 is set from 0 to 2**n-1
    """
    num_outcome = 2**len(hand)   
    temp_set = set([()])
    
    for dummy_x in range(1, num_outcome):
        # 5 on converting to binary results 0b101.
        # We ignore the first two digits
        index_list = gen_ones_set(bin(dummy_x)[2::])
        temp_tuple = ()
        for dummy_y in index_list:
            temp_tuple = temp_tuple + (hand[dummy_y],)
        temp_set.add(temp_tuple)
        
gen_all_subsets_bin((1, 2, 3))

#print gen_all_sequences((1, 2), 2)

"""
tuple_1 = ()
temp_set = set([()])
x = 1
tuple_1 = tuple_1 + (x,)
tuple_1 = tuple_1 + (2,)
tuple_1 = tuple_1 + (3,)
print tuple_1
temp_set.add(tuple_1)
print temp_set
"""