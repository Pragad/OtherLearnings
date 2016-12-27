"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor

codeskulptor.set_timeout(20)

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
        # Eg: 5 on converting to binary results 0b101.
        # We ignore the first two digits
        index_list = gen_ones_set(bin(dummy_x)[2::])
        temp_tuple = ()
        for dummy_y in index_list:
            temp_tuple = temp_tuple + (hand[dummy_y],)
        temp_set.add(temp_tuple)
    
    return temp_set

def find_outcomes(length):
    """
    Computes the possible numbers from 1 to length and stores
    them in a list.
    """
    outcomes = []
    for dummy_x in range(1, length+1):
        outcomes.append(dummy_x)
    return outcomes

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    # sum_score holds the sum of consecutive integers
    if (not hand):
        return 0
    
    max_score = hand[0]
    sum_score = hand[0]
    
    for dummy_x in range(1, len(hand)):
        if (hand[dummy_x] == hand[dummy_x-1]):
            sum_score += hand[dummy_x]
        else:
            sum_score = hand[dummy_x]
            
        if (sum_score > max_score):
            max_score = sum_score
        if (hand[dummy_x] > max_score):
            max_score = hand[dummy_x]

    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = find_outcomes(num_die_sides)
    all_free_seq = gen_all_sequences(outcomes, num_free_dice)
    all_seq = []
    
    for dummy_x in all_free_seq:
        all_seq.append(tuple(sorted(held_dice + dummy_x)))
       
    total_score = 0
    for dummy_x in all_seq:
        total_score += score(dummy_x)
    return float(total_score)/len(all_seq)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_subsets = gen_all_subsets_bin(hand)
    return all_subsets


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    max_exp_val = 0
    to_hold = ()
    for dummy_x in all_holds:
        print dummy_x, num_die_sides, len(hand) - len(dummy_x)
        temp_max_exp_val = expected_value(dummy_x, num_die_sides, len(hand) - len(dummy_x))
        if (max_exp_val < temp_max_exp_val):
            max_exp_val = temp_max_exp_val
            to_hold = dummy_x
    return (max_exp_val, to_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
#run_example()

#import user40_zT7QUS4ixa_25 as yahtzee_testsuite
#yahtzee_testsuite.run_score_suite(score)
#yahtzee_testsuite.run_exp_val_suite(expected_value)
#yahtzee_testsuite.run_gen_all_holds_suite(gen_all_holds)
#yahtzee_testsuite.run_strategy_suite(strategy)
