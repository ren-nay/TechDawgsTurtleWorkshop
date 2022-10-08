# We will begin by importing the Turtle module. The process of importing allows for code in another module to be available within our script. 
# Here we are importing the Turtle module, which is a module that contains code pertaining to moving and drawing with a cursor/turtle.

# The Python language gives us a few methods that we can use to import a module. The first of which is simply typing 'import <module>'
# When a module is imported this way we must remember to prefix its provided code with the name of the module. For instance:
#       import my_module
#       my_module.do_something()
# We can further simplify this by giving our imported a module an alias, or new name.
#       import my_module as mm
#       mm.do_something()
# If we want to fully remove the prefix on our code or only bring in some of the code in a module, we can also import like this:
#       from my_module import * # Note the '*', this means we want everything in the module!
#       do_something()
# We will opt for using the from <module> import <> approach 

from turtle import *

# Notice that if we run our script right now nothing of note will happen. This is because we haven't given the computer any instructions on 
# how it should use the Turtle module. So lets fix that by telling the Turtle module to draw a dot for us. This can be done using Turtle's
# 'dot()' function! So lets write the dot instruction and run our code.

dot()

# Notice that now when we run the code a window briefly appears and instantly closes, this is due to the fact that our code has finished
# all of its instructions and has nothing else to run or stay on. We can fix this by using Turtles 'done()' function, to prevent our 
# program from closing our window. This is also how we should end all of our turtle commands.

#done() <- commented out for use later.

# Notice that now we see our drawn dot in the middle of the window, but we also see a weird triangle shape near it. This is our cursor or 'turtle'
# and is the the location in which our instructions affect the window. So lets proceed by changing our cursor to actually look like a turtle using
# the the shape() function with the argument 'turtle'. Once added be sure to move your done() instruction to after your final instruction.

shape("turtle")
































done()