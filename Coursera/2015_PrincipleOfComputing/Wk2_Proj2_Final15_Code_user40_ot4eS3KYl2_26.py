"""
Clone of 2048 game.
"""


import random
#import user40_bJHRdpmDGW_19 as poc_2048_testsuite

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

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
    Helper function that merges a single row or column in 2048
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

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_rows = grid_height
        self._grid_cols = grid_width
        self._grid = []
        
        # Added reset to initialize the grid
        self.reset()
        
        self._initial_tiles_up = []
        self._initial_tiles_down = []
        self._initial_tiles_left = []
        self._initial_tiles_right = []
        
        # Computing initial list for Move function.
        # If  UP
        # tiles = 00, 01, 02, 03 ...
        # 0 till width of the grid
        for temp in range(self._grid_cols):
            self._initial_tiles_up.append(temp)
        
        # If Down
        # tiles = h0 h1 h2 h3 ...
        # h*10+0, h*10+1, ...
        for temp in range(self._grid_cols):
            self._initial_tiles_down.append(((self._grid_rows -1) * 10) + temp)
        
        # If Left
        # tiles = 00, 10, 20, 30 ...
        # 0 till height of grid * 10 AND 0
        for temp in range(self._grid_rows):
            self._initial_tiles_left.append(temp * 10)
        
        # If Right
        # tiles = 0w, 1w, 2w, 3w ..
        # 0 till height of grid * 10 AND w
        for temp in range(self._grid_rows):
            self._initial_tiles_right.append(temp * 10 + (self._grid_cols -1))      

        # Creating a dictionary. Key is the direction and Value
        # is the List of initial tiles corresponding to that
        # direction.
        self._initial_tiles_dict = {}
        self._initial_tiles_dict[UP] = self._initial_tiles_up
        self._initial_tiles_dict[DOWN] = self._initial_tiles_down
        self._initial_tiles_dict[LEFT] = self._initial_tiles_left
        self._initial_tiles_dict[RIGHT] = self._initial_tiles_right
             
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_x in range(self._grid_cols)] for dummy_x in range(self._grid_rows)]
        
        # Initalize the grid with two tiles to start the game
        self.new_tile()
        # print self._grid
        self.new_tile()
        # print self._grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)
        #str_grid = ' '.join(str(element) for element in self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_cols

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        size_of_temp_list = 0
        #self._initial_tiles_dict[direction]
        
        if (direction == UP or direction == DOWN):
            size_of_temp_list = len(self._initial_tiles_dict[direction + 2])
        else:
            size_of_temp_list = len(self._initial_tiles_dict[direction - 2])
        
        #print "\nGrid: \n", self._grid
        
        old_grid = []
        for item in self._grid:
            old_grid.append(list(item))
            
        for count in range(len(self._initial_tiles_dict[direction])):
            temp_list = []
            row_index = self._initial_tiles_dict[direction][count] / 10
            col_index = self._initial_tiles_dict[direction][count] % 10
            for dummy_temp_list_count in range(size_of_temp_list):

                temp_list.append(self.get_tile(row_index, col_index))

                row_index += OFFSETS[direction][0]
                col_index += OFFSETS[direction][1]

            temp_list = merge(temp_list)
            
            m_row_index = self._initial_tiles_dict[direction][count] / 10
            m_col_index = self._initial_tiles_dict[direction][count] % 10            
            for temp_merge_list_cnt in range(len(temp_list)):
                self.set_tile(m_row_index, m_col_index, temp_list[temp_merge_list_cnt])
                m_row_index += OFFSETS[direction][0]
                m_col_index += OFFSETS[direction][1]
        
        # Should add a new tile only when some change has been done
        # to the existing grid
        # Should do a deep copy to copy the list
        new_grid = []
        for item in self._grid:
            new_grid.append(list(item))
            
        if (old_grid != new_grid):
            self.new_tile()
        
    def get_empty_tiles(self):
        """
        Scan through the entire grid and create a new list
        that has all the empty cells. New list will be of
        the form ROW*10 + COL*1
        """  
        empty_tiles = []
        for row_index in range(self.get_grid_height()):
            for col_index in range(self.get_grid_width()):
                if (self.get_tile(row_index, col_index) == 0):
                    empty_tiles.append(row_index * 10 + col_index)
                    
        return empty_tiles
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        available_numbers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        
        # Find empty tiles and choose one at random
        empty_tiles = self.get_empty_tiles()
        # print "grid: ", self._grid
        # print "empty_tiles: ", empty_tiles
        if (len(empty_tiles) != 0):
            random_empty_cell = empty_tiles[random.randint(0,len(empty_tiles)-1)]
            random_empty_cell_row = random_empty_cell / 10
            random_empty_cell_col = random_empty_cell % 10
            random_empty_cell_num = available_numbers[random.randint(0,9)]
            # Fill the randomly chosen empty tile with either 2 or 4
            self.set_tile(random_empty_cell_row, 
                          random_empty_cell_col,
                          random_empty_cell_num)
            # print "Row: ", random_empty_cell_row," Col: ", random_empty_cell_col," Num: ", random_empty_cell_num
        else:
            print "\nGame Over\n\n"
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        
        if ((row >= 0 and
             row < self.get_grid_height()) and 
            (col >= 0 and
             col < self.get_grid_width())):
            self._grid[row][col] = value
        """
        self._grid[row][col] = value

        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """          
        return self._grid[row][col]

# Create tests to check the correctness of your code
# import test suite and run
#poc_2048_testsuite.run_suite(TwentyFortyEight)
    
import poc_2048_gui
poc_2048_gui.run_gui(TwentyFortyEight(3, 4))