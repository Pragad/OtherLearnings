"""
Test suite for the ClickerState class
"""

import codeskulptor
import math
import poc_simpletest
import poc_clicker_provided as provided
import user40_DpynmIvl2b_53 as clicker_state_implementation


# Test for Phase 1
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
    suite.run_test(str(clicker_state), "Time: 0.0, Current Cookies: 0.0, CPS: 1.0, Total Cookies: 0.0", "__str__")
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
    suite.run_test(str(clicker_state), "Time: 1.0, Current Cookies: 1.0, CPS: 1.0, Total Cookies: 1.0", "__str__")
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
    suite.run_test(str(clicker_state), "Time: 1.0, Current Cookies: 0.0, CPS: 2.0, Total Cookies: 1.0", "__str__")
    suite.run_test(clicker_state.time_until(0), 0.0, "time until 0")
    suite.run_test(clicker_state.time_until(2), 1.0, "time until 2")    
    
    suite.report_results()      

    
# run tests for Phase 1
print "Initializing a ClickerState object"
clicker_state = clicker_state_implementation.ClickerState() 
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

print "\nattempting to buy item  for 2.0 cookies for 1.0 extra cps"
clicker_state.buy_item("name", 2.0, 1.0)
run_wait_1_suite(clicker_state)

print "\nbuying an item for 1.0 cookies for 1.0 extra cps"
clicker_state.buy_item("name", 1.0, 1.0)
run_buy_1_1_suite(clicker_state)


# Tests for Phase 2
def run_strategy_cursor_broken_suite(clicker_state):
    """
    strategy_cursor_broken testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(round(clicker_state.get_cookies(), 1), 6965195661.5 , "get_cookies")
    suite.run_test(clicker_state.get_time(), 10000000000.0, "get_time")
    suite.run_test(round(clicker_state.get_cps() ,1), 16.1 , "get_cps")
    #suite.run_test(str(round(clicker_state.get_history()[-1][3], 1)), "153308849166.0", "total_cookies")  
    suite.run_test(str(clicker_state.get_total_cookies()), "153308849166.0", "total_cookies")  
   
    suite.report_results() 

def run_strategy_cursor_broken_suite_2(clicker_state):
    """
    strategy_cursor_broken testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(str(clicker_state.get_cookies()), "28.0735995433", "get_cookies")
    suite.run_test(clicker_state.get_time(), 500.0, "get_time")
    suite.run_test(round(clicker_state.get_cps() ,1), 2.7, "get_cps")
    #suite.run_test(str(round(clicker_state.get_history()[-1][3], 1)), "153308849166.0", "total_cookies")  
    suite.run_test(str(clicker_state.get_total_cookies()), "1004.2", "total_cookies")  
   
    suite.report_results()   

def run_strategy_cursor_broken_suite_3(clicker_state):
    """
    strategy_cursor_broken testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test clicker_state
    suite.run_test(str(clicker_state.get_cookies()), "13.9125", "get_cookies")
    suite.run_test(clicker_state.get_time(), 16.0, "get_time")
    suite.run_test(round(clicker_state.get_cps() ,1), 151.0, "get_cps")
    #suite.run_test(str(round(clicker_state.get_history()[-1][3], 1)), "153308849166.0", "total_cookies")  
    suite.run_test(str(clicker_state.get_total_cookies()), "66.0", "total_cookies")  
   
    suite.report_results()   
    
# Run tests for Phase 2
print "\nRunning strategy_cursor_broken 1"
clicker_state = clicker_state_implementation.simulate_clicker(provided.BuildInfo(),
                                                              clicker_state_implementation.SIM_TIME,
                                                              clicker_state_implementation.strategy_cursor_broken)
run_strategy_cursor_broken_suite(clicker_state)

print "\nRunning strategy_cursor_broken 2"
clicker_state_2 = clicker_state_implementation.simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), \
                                                                500.0, clicker_state_implementation.strategy_cursor_broken)
run_strategy_cursor_broken_suite_2(clicker_state_2)

print "\nRunning strategy_cursor_broken 3"
clicker_state_3 = clicker_state_implementation.simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), \
                                                                16.0, clicker_state_implementation.strategy_cursor_broken)
run_strategy_cursor_broken_suite_3(clicker_state_3)
