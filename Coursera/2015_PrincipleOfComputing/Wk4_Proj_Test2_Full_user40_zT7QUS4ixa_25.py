"""
Template testing suite for 2048
"""

import poc_simpletest

def run_score_suite(score_function):
    """
    Testing code for score function
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    print "\nTesting score function"
    
    # test format_function on various inputs
    suite.run_test(score_function((1, 1, 1, 5, 6)), 6, "Test #1:")
    suite.run_test(score_function((1, 1, 1, 1, 4)), 4, "Test #2:")
    suite.run_test(score_function((1, 2, 3, 5, 6)), 6, "Test #3:")
    suite.run_test(score_function((1, 1, 2, 2, 3)), 4, "Test #4:")
    suite.run_test(score_function((2, 2, 3, 3, 3)), 9, "Test #5:")
    suite.run_test(score_function((2, 2, 2, 3, 3)), 6, "Test #6:")
    suite.run_test(score_function((1, 1, 3, 3, 5)), 6, "Test #7:")
    suite.run_test(score_function((2, 2, 3, 4, 6)), 6, "Test #8:")
    suite.run_test(score_function((1, 1, 3, 4, 5)), 5, "Test #9:")
    suite.run_test(score_function((1, 1, 2, 2, 5)), 5, "Test #10:")
    suite.run_test(score_function((2, 2, 2, 2, 2)), 10, "Test #11:")
    suite.run_test(score_function(()), 0, "score 1,")
    suite.run_test(score_function((1,)), 1, "score 1,")
    suite.run_test(score_function((1, 1)), 2, "score 1,1")
    suite.run_test(score_function((1, 1, 3, 5, 5, 6)), 10, "score 1,1,3,5,5,6")
    suite.run_test(score_function((1, 1, 3, 5, 6, 6)), 12, "score 1,1,3,5,6,6")

    # test contributed by Karthink Balakrishnan
    suite.run_test(score_function((3, 3, 9, 8)), 9, "score 3,3,9,8")    
    suite.report_results()
    
def run_exp_val_suite(expected_value_function):
    """
    Testing code for expected_value function
    """
    # create a TestSuite object    
    suite = poc_simpletest.TestSuite()
    print "\nTesting expected_value function"
    
    suite.run_test(expected_value_function((2,2), 6, 2), float(210)/36, "Test #12:")
    suite.run_test(expected_value_function((), 6, 2), float(182)/36, "Test #13:")
    
    suite.run_test(expected_value_function((), 1, 1), 1, "expected value: held:(), sides:1, rolls:1")
    suite.run_test(expected_value_function((1,), 1, 1), 2, "expected value: held:(1,), sides:1, rolls:1")
    suite.run_test(expected_value_function((1,), 1, 2), 3, "expected value: held:(1,), sides:1, rolls:2")
    suite.run_test(expected_value_function((1,), 2, 1), 2, "expected value: held:(1,), sides:2, rolls:1")
    suite.run_test(expected_value_function((1,), 2, 2), 2.75, "expected value: held:(1), sides:2, rolls:2")
#   1,1,1, = 3; 1,1,2 = 2; 1,2,1 = 2; 1,2,2 = 4 -> 11/4 = 2.75

    suite.run_test(expected_value_function((1,), 4, 1), 2.75, "expected value: held:(1), sides:4, rolls:1")
#	1,1 = 2; 1,2 = 2, 1,3 = 3, 1,4 = 4  -> 11/4 = 2.75

    suite.run_test(expected_value_function((1, 1), 1, 1), 3, "expected value: held:(1,1), sides:1, rolls:1")
    suite.run_test(expected_value_function((1, 1), 1, 2), 4, "expected value: held:(1,1), sides:1, rolls:2")
    suite.run_test(expected_value_function((1, 1), 2, 1), 2.5, "expected value: held:(1,1), sides:2, rolls:1")
    suite.run_test(expected_value_function((1, 2), 2, 1), 3, "expected value: held:(1,2), sides:1, rolls:1")
    suite.run_test(expected_value_function((1, 2), 2, 2), 4.25, "expected value: held:(1,2	), sides:1, rolls:2")
    
    suite.run_test(expected_value_function((3, 3), 8, 5),372212.0/32768,"8-sided die ")
    # suite.run_test(yahtzee_function((1, 5, 6, 6, 6), 9), (58.0/3,(6,6,6)), "9-sided die")
    
    # report number of tests and failures
    suite.report_results()
    
def run_gen_all_holds_suite(gen_all_holds_function):
    """
    Testing code for gen_all_holds function
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_holds on various inputs
    print "\nTesting gen_all_holds function"
    suite.run_test(gen_all_holds_function((1,)), set([(), (1,)]), "gen_all_holds 1")
    suite.run_test(gen_all_holds_function((1, 2)), set([(), (1,), (2,), (1,2)]), "gen_all_holds 1,2")
    suite.run_test(gen_all_holds_function((1, 1)), set([(), (1,), (1,1)]), "gen_all_holds 1,1")
    suite.run_test(gen_all_holds_function((1, 1, 2)), set([(), (1,), (2,), (1,1), (1,2), (1,1,2)]), "gen_all_holds 1,1,2")
    suite.run_test(gen_all_holds_function((1, 1, 2, 2)), set([(), (1,), (2,), (1,1), (1,2), (2,2), (1,1,2), (1,2,2), (1,1,2,2)]), "gen_all_holds 1,1,2,2")
    suite.run_test(gen_all_holds_function((1, 2, 3)), set([(), (1,), (2,), (3,), (1,2), (2,3), (1,3), (1,2,3)]), "gen_all_holds 1,2,3")
    
    # test case stolen from Doug Lefelhocz' forum message
    suite.run_test(gen_all_holds_function((1, 2, 2, 3)), set([(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 2), (2, 3), (1, 2, 2), (1, 2, 3), (2, 2, 3), (1, 2, 2, 3)]), "gen_all_holds 1,2,2,3")    
    
    suite.report_results()
    
    
def run_strategy_suite(strategy_suite_function):
    """
    Testing code for strategy function: strategy(hand, num_die_sides)
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test strategy on various inputs
    print "\nTesting strategy function"
    #suite.run_test(strategy_suite_function((6), 6), (6.0, (6,)), "rolled 6")
    suite.run_test(strategy_suite_function((6,), 6), (6.0, (6,)), "rolled 6,")
    #suite.run_test(strategy_suite_function((1), 6), (3.5, ()), "rolled 1")
    suite.run_test(strategy_suite_function((1,), 6), (3.5, ()), "rolled 1,")
    suite.run_test(strategy_suite_function((6,6), 6), (12.0, (6,6)), "rolled 6,6")
    
#    Two Equally successful strategies
#    suite.run_test(strategy_suite_function((1,1), 1), (2.0, (1,1)), "rolled 1,1 of 1")
#    suite.run_test(strategy_suite_function((1,1), 1), (2.0, ()), "rolled 1,1 of 1")

    suite.run_test(strategy_suite_function((1,1), 2), (2.5, ()), "rolled 1,1 of 2")
    suite.run_test(strategy_suite_function((1,6), 6), (7.0, (6,)), "rolled 1,6")
    suite.run_test(strategy_suite_function((1,6,6), 6), (13.0, (6,6)), "rolled 1,6,6")
    suite.run_test(strategy_suite_function((1,2), 2), (3.0, (2,)), "rolled 1,2 of 2")
    suite.run_test(strategy_suite_function((1,4,4), 6), (8+2.0/3,(4,4)), "rolled 1,4,4")
    # Test contributed by Doron Chosnek
    suite.run_test(strategy_suite_function((1, 5, 6, 6, 6), 9), (58.0/3,(6,6,6)), "9-sided die")
    
    suite.report_results()    