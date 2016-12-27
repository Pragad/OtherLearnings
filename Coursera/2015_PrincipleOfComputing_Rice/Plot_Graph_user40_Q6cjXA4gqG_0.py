"""
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot
import math

# create three sample functions

def double(num):
    """
    Example of linear function
    """
    return 2 * num

def square(num):
    """
    Example of quadratic function
    """
    return num ** 2

def exp(num):
    """
    Example of exponential function
    """
    return 2 ** num


def create_plots(begin, end, stride):
    """ 
    Plot the function double, square, and exp
    from beginning to end using the provided stride
    
    The x-coordinates of the plotted points start
    at begin, terminate at end and are spaced by 
    distance stride
    """
    
    # generate x coordinates for plot points
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride
        
    # compute list of (x, y) coordinates for each function
    double_plot = [(x_val, double(x_val)) for x_val in x_coords]
    square_plot = [(x_val, square(x_val)) for x_val in x_coords]
    exp_plot = [(x_val, exp(x_val)) for x_val in x_coords]
    
    # plot the list of points
    simpleplot.plot_lines("Plots of three functions", 600, 400, "x", "f(x)",
                         [double_plot, square_plot, exp_plot], 
                         True, ["double", "square", "exp"])
   
#create_plots(0, 2, .1)
                          
                   
    
def func1(days): 
    return math.e ** (9.5*days)
    
def func2(days):
    return 95 * days ** 2

def func3(days):
    return math.e ** (0.095 * days)

def func4(days):
    return 9.5 * days ** 4

def create_plots_2(begin, end, stride):
    
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride
        
    func1_plot = [(x, func1(x)) for x in x_coords]
    func2_plot = [(x, func2(x)) for x in x_coords]
    func3_plot = [(x, func3(x)) for x in x_coords]
    func4_plot = [(x, func4(x)) for x in x_coords]
    # plot the list of points
    simpleplot.plot_lines("Plots of four functions", 600, 400, "x", "f(x)",
                         [func1_plot, func2_plot, func3_plot, func4_plot], 
                         True, ["1", "2", "3", "4"])
             
   
create_plots_2(0, 2, 0.1)
