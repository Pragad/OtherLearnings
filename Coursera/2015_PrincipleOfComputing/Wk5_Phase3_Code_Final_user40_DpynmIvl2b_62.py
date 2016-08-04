
"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(600)

import poc_clicker_provided as provided
import math

# Constants
#SIM_TIME = 10000000000.0
SIM_TIME = 100.0
#SIM_TIME = 5000.0
ERROR_LOGGING = 0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._num_total_cookies = 0.0
        self._num_curr_cookies  = 0.0
        self._curr_time_secs    = 0.0
        self._curr_cps          = 1.0
        self._game_history      = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        #return str([self._num_total_cookies,
        #        self._num_curr_cookies,
        #        self._curr_time_secs,
        #        self._curr_cps])
        return str("Time: " +
                   str(self.get_time()) +
                   ", Current Cookies: " +
                   str(self.get_cookies()) +
                   ", CPS: " +
                   str(self.get_cps()) + 
                   ", Total Cookies: " +
                   str(self.get_total_cookies()))
     
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._num_curr_cookies
    
    def get_total_cookies(self):
        """
        Return total number of cookies 
        
        Should return a float
        """
        return self._num_total_cookies
        
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._curr_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._curr_time_secs
    
    def append_history(self, cur_time, bought_item, item_cost, total_cookies):
        """
        Update the history list
        """
        temp_history = (cur_time, bought_item, item_cost, total_cookies)
        self._game_history.append(temp_history)
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        temp_history = self._game_history[:]
        return temp_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if (self.get_cookies() >= cookies):
            return 0.0
        else:
            return math.ceil(float(cookies - self.get_cookies())/self.get_cps())
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        temp_time = math.floor(time)
        if (math.floor(time) > 0.0):
            self._num_curr_cookies  += temp_time * self.get_cps()
            self._curr_time_secs    += temp_time
            #self._num_total_cookies += self.get_cookies()
            self._num_total_cookies += temp_time * self.get_cps()
        else:
            pass
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (cost <= self.get_cookies()):
            self._curr_cps += additional_cps
            self._num_curr_cookies -= cost
            self.append_history(self.get_time(), 
                                item_name,
                                cost,
                                self.get_total_cookies())
        else:
            pass
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    dup_build_info = build_info.clone()
    obj_clicker_state = ClickerState()
    
    while (obj_clicker_state.get_time() < duration):
        if ERROR_LOGGING:
            print "Cur time: ", obj_clicker_state.get_time(), \
                  ", Duration: ", duration
            print str(obj_clicker_state)
            #print dup_build_info._info["Cursor"]
        item_to_buy = strategy(obj_clicker_state.get_cookies(),
                               obj_clicker_state.get_cps(),
                               obj_clicker_state.get_history(),
                               duration - obj_clicker_state.get_time(),
                               dup_build_info)
        
        # Break if we don't have to buy any item
        if (item_to_buy == None):
            break
        
        # Break if the state's get time is more than the simulation time
        if (obj_clicker_state.get_time() > duration):
            break
                        
        item_to_buy_cost = dup_build_info.get_cost(item_to_buy)
        time_to_wait = obj_clicker_state.time_until(item_to_buy_cost)
        
        if ERROR_LOGGING:
            print "Item: ", item_to_buy, \
                  ", Cost: ", item_to_buy_cost, \
                  ", Wait time: ", time_to_wait 
        
        #  If we would have to wait past the duration of the 
        # simulation to purchase the item, we should end the simulation. 
        if (time_to_wait > \
            duration - obj_clicker_state.get_time()):
            break
            
        obj_clicker_state.wait(time_to_wait)
        obj_clicker_state.buy_item(item_to_buy, 
                                   item_to_buy_cost, 
                                   dup_build_info.get_cps(item_to_buy))

        dup_build_info.update_item(item_to_buy)
        
        if ERROR_LOGGING:
            print obj_clicker_state.get_history(), "\n"
    
    # If we have some time left, buy cookies with the current setup
    # Even if there is No time left, at the last second, buy
    # whatever you can
    if (obj_clicker_state.get_time() <= duration):
        remaining_time = duration - obj_clicker_state.get_time()
        obj_clicker_state.wait(remaining_time)
        
        if ERROR_LOGGING:
            print "IF: ", str(obj_clicker_state)
            print "IF: ", obj_clicker_state.get_history(), "\n"  
        
        # Buy item at the last. A newly added module
        item_to_buy = strategy(obj_clicker_state.get_cookies(),
                               obj_clicker_state.get_cps(),
                               obj_clicker_state.get_history(),
                               duration - obj_clicker_state.get_time(),
                               dup_build_info)
        
        # Break if we don't have to buy any item
        if (item_to_buy != None):
            item_to_buy_cost = dup_build_info.get_cost(item_to_buy)
            #print item_to_buy_cost
            obj_clicker_state.buy_item(item_to_buy, 
                                       item_to_buy_cost, 
                                       dup_build_info.get_cps(item_to_buy))

            dup_build_info.update_item(item_to_buy)        
            
            if ERROR_LOGGING:
                print "IF: ", str(obj_clicker_state)
    
    return obj_clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cookies_affordable = cps * time_left
    items_list = build_info.build_items()
    min_cost = float("inf")
    min_index = float("inf")
    for index in range(len(items_list)):
        temp_cost = build_info.get_cost(items_list[index])
        if ((min_cost > temp_cost) and 
            (cookies + cookies_affordable >= temp_cost)):
            min_cost = temp_cost
            min_index = index
    
    if (min_index != float("inf")): 
        if ERROR_LOGGING:
            print items_list[min_index]        
            
        return items_list[min_index]
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    cookies_affordable = cps * time_left
    items_list = build_info.build_items()
    max_cost = float("-inf")
    max_index = float("-inf")
    for index in range(len(items_list)):
        temp_cost = build_info.get_cost(items_list[index])
        if ((max_cost < temp_cost) and 
            (cookies + cookies_affordable >= temp_cost)):
            max_cost = temp_cost
            max_index = index
        
    if (max_index != float("-inf")):
        if ERROR_LOGGING:
            print items_list[max_index]

        return items_list[max_index]
    else:
        return None    

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("None", SIM_TIME, strategy_none)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
#run()

#simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), \
#                 5000.0, strategy_none)
#simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), \
#                 500.0, strategy_cursor_broken)
#simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), \
#                 16.0, strategy_cursor_broken)

#strategy_cheap(2.0, 1.0, [(0.0, None, 0.0, 0.0)], 1.0, \
#               provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))

#strategy_cheap(1.0, 3.0, [(0.0, None, 0.0, 0.0)], 17.0, \
#               provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))