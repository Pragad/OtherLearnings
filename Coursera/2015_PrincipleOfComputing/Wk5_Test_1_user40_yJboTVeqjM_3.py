"""
Test suite for the ClickerState class
"""

import codeskulptor
import poc_simpletest
import user40_DpynmIvl2b_23 as clicker_state_implementation


def run_initialization_suite(clicker_state):
    """
    Initialization testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(clicker_state.get_cookies(), 0.0, "get_cookies")
    suite.run_test(clicker_state.get_time(), 0.0, "get_time")
    suite.run_test(clicker_state.get_cps(), 1.0, "get_cps")
    suite.run_test(clicker_state.get_history(), [(0.0, None, 0.0, 0.0)] , "get_history")
    suite.run_test(str(clicker_state), "cookies: 0.0, time: 0.0, cps: 1.0", "__str__")
    suite.run_test(clicker_state.time_until(0), 0.0, "time until 0")
    suite.run_test(clicker_state.time_until(2), 2.0, "time until 2")    
    
    suite.report_results()
    

def run_wait_1_suite(clicker_state):
    """
    wait(1) testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(clicker_state.get_cookies(), 1.0, "get_cookies")
    suite.run_test(clicker_state.get_time(), 1.0, "get_time")
    suite.run_test(clicker_state.get_cps(), 1.0, "get_cps")
    suite.run_test(str(clicker_state), "cookies: 1.0, time: 1.0, cps: 1.0", "__str__")
    suite.run_test(clicker_state.time_until(0), 0.0, "time until 0")
    suite.run_test(clicker_state.time_until(2), 1.0, "time until 2")    
    
    suite.report_results()    
    

def run_buy_1_1_suite(clicker_state):
    """
    buy item 1 for 1 testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(clicker_state.get_cookies(), 0.0, "get_cookies")
    suite.run_test(clicker_state.get_time(), 1.0, "get_time")
    suite.run_test(clicker_state.get_cps(), 2.0, "get_cps")
    suite.run_test(clicker_state.get_history(), [(0.0, None, 0.0, 0.0), (1.0, "name", 1.0, 1.0)] , "get_history")
    suite.run_test(str(clicker_state), "cookies: 0.0, time: 1.0, cps: 2.0", "__str__")
    suite.run_test(clicker_state.time_until(0), 0.0, "time until 0")
    suite.run_test(clicker_state.time_until(2), 1.0, "time until 2")    
    
    suite.report_results()      
    

# create a ClickerState object
clicker_state = clicker_state_implementation.ClickerState()   
    
print "initialization"
run_initialization_suite(clicker_state)

print "\nwaiting 0"
clicker_state.wait(0)
run_initialization_suite(clicker_state)

print "\nwaiting -1"
clicker_state.wait(-1)
run_initialization_suite(clicker_state)

print "\nwaiting 1"
clicker_state.wait(1)
run_wait_1_suite(clicker_state)

print "\nwaiting 0.5"
clicker_state.wait(0.5)
run_wait_1_suite(clicker_state)

print "\nattempt to buy item  for 2.0 cookies for 1.0 extra cps"
clicker_state.buy_item("name", 2.0, 1.0)
run_wait_1_suite(clicker_state)

print "\nbuy item for 1.0 cookies for 1.0 extra cps"
clicker_state.buy_item("name", 1.0, 1.0)
run_buy_1_1_suite(clicker_state)

