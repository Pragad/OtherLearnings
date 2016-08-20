# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60 
    #print seconds_in_minute
    

clock_helper(90)

my_string = "hello"
#print my_string
#print my_string[-1]
## print my_string.last()
##print my_string.pop()
## print my_string[len(my_string)]

val1 = [1, 2, 3]
val2 = val1[1:]
#print val2
val1[2]  = 4

#print val2
#print val2[1]
#print val1

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for count in range(25):
        sum = 0
        lst2 = lst[-3:]
        sum = sum + lst2[0] + lst2[1] + lst2[2]
        lst.append(sum)
    return lst
    
sum_three = [0, 1, 2]
appendsums(sum_three)

print sum_three[10]   
print sum_three[20]
