"""
Template testing suite for 2048
"""

import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class(2,2)
    
    # add tests using suite.run_test(....) here

    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([]), "Test #0: init")
    
    # suite.run_test(game.reset(), str([]), "Test #1: reset")
    game.reset()
    suite.run_test(str(game), str([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), "Test #1: reset")

    suite.run_test(game.get_grid_height(), 2 , "Test #2: get_grid_height")
    suite.run_test(game.get_grid_width(), 3 , "Test #3: get_grid_width")
    
    game.set_tile(0, 0, 5)
    game.set_tile(0, 1, 5)
    game.set_tile(1, 0, 5)
    game.set_tile(1, 1, 5)
    game.set_tile(2, 0, 5)
    game.set_tile(0, 2, 5)
    game.set_tile(2, 2, 5)
    game.set_tile(-1, 2, 5)
    #game.set_tile(, , 5)
    #game.move(UP)
    #game.move(DOWN)
    #game.move(LEFT)
    #game.move(RIGHT)
    
    # report number of tests and failures
    suite.report_results()
