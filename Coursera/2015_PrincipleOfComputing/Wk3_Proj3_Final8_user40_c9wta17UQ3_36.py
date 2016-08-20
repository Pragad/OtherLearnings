"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 5         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
    
def mc_trial(board, player):
    """
    The following function takes a board and a starting 
    player and plays till the game is over.
    """   
    while (board.check_win() == None):
        # Get list of empty squares and select one row-col
        # at random
        empty_squares = board.get_empty_squares()
        rand_row_col_index =  random.randrange(0,len(empty_squares))
        rand_row = empty_squares[rand_row_col_index][0]
        rand_col = empty_squares[rand_row_col_index][1]
        
        # Add player entry at that row-col and break if 
        # game is won. Else switch the player and continue
        # the loop
        board.move(rand_row, rand_col, player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    The following function updates the score matrix
    """    
    
    # If the game is a draw then the score remains the same.
    player_won = board.check_win()
    if (player_won == provided.DRAW):
        return
    
    if (player_won == player):
        for dummy_x in range (board.get_dim()):
            for dummy_y in range (board.get_dim()):
                if (board.square(dummy_x,dummy_y) == player):
                    scores[dummy_x][dummy_y] += SCORE_CURRENT
                elif (board.square(dummy_x,dummy_y) == provided.switch_player(player)):
                    scores[dummy_x][dummy_y] -= SCORE_CURRENT    
    else:
        for dummy_x in range (board.get_dim()):
            for dummy_y in range (board.get_dim()):
                if (board.square(dummy_x,dummy_y) == player):
                    scores[dummy_x][dummy_y] -= SCORE_CURRENT
                elif (board.square(dummy_x,dummy_y) == provided.switch_player(player)):
                    scores[dummy_x][dummy_y] += SCORE_CURRENT          

def get_best_move(board, scores):
    """
    The following function gets the best move by comparing
    the board with the scores matrix
    Input: board matrix, scores matrix
    Output: A tuple of row,col that has the max value in scores
    """    
    
    # First traverse the list of scores and find the maximum
    # element.
    # Maximum will be the first non-empty score to start with    
    empty_squares = board.get_empty_squares()
    max_elements = []
    maximum = scores[empty_squares[0][0]][empty_squares[0][1]]
   
    if empty_squares:
        for dummy_x in empty_squares:
            if (maximum < scores[dummy_x[0]][dummy_x[1]]):
                maximum = scores[dummy_x[0]][dummy_x[1]]
 
        #Then traverse the list of empty squares and
        # find all squares that has the maximum element 
        # and add it to a list
        for dummy_x in empty_squares:
            if (maximum == scores[dummy_x[0]][dummy_x[1]]):
                max_elements.append(dummy_x)

        # Choose one square with max value at random and
        # return it
        return max_elements[random.randrange(0,len(max_elements))]

def mc_move(board, player, trials):
    """
    The following function plays several trials and chooses
    the best move.
    """ 
    scores = [[0 for dummy_x in range(board.get_dim())] for dummy_x in range(board.get_dim())]
    for dummy_x in range(trials):
        temp_board = board.clone()
        mc_trial(temp_board, player)
        mc_update_scores(scores, temp_board, player)
    return get_best_move(board, scores)
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
