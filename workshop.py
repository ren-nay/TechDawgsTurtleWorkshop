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

#dot()

# Notice that now when we run the code a window briefly appears and instantly closes, this is due to the fact that our code has finished
# all of its instructions and has nothing else to run or stay on. We can fix this by using Turtles 'done()' function, to prevent our 
# program from closing our window. This is also how we should end all of our turtle commands.

#done() <- commented out for use later.

# Notice that now we see our drawn dot in the middle of the window, but we also see a weird triangle shape near it. This is our cursor or 'turtle'
# and is the the location in which our instructions affect the window. So lets proceed by changing our cursor to actually look like a turtle using
# the shape() function with the argument 'turtle'. Once added be sure to move your done() instruction to after your final instruction.

shape("turtle")

# I suppose now we ought to give our turtle a name, so lets call ours Shelly!  Lets have Shelly write its name for us!

# write("Hello! My name is Shelly")
#done()

# Well that is some uniform handwriting, it appears Shelly has many talents!
# Lets use shelly to draw a quick line. This can be done by simply telling
# Shelly to move forward some number of units with the "forward(number)" function. Let's try it out!

#forward(10)

# Wow! Shelly has now moved ahead 150 units on our grid, lets make this a bit more interesting by changing the color of Shelly's trail with the "color("color") 
# function!
# Most colors will work, so long as we declare it as a string, we'll tell Shelly to use blue.

#color("blue")
#forward(100)
#done()

# Lets try something a bit more complicated with some of the Python syntax we learned earlier. Let's try getting our turtle to draw a square!
# We can accomplish this in a few ways, the most straight forward approach would be to directly tell Shelly what to do every time. So let's try 
# that. Notice we will now be using some new functions from the turtle module as well, those being the "left(number)" and "right(number)" functions.

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# done()

# Well that wasn't too difficult, but its kinda redundant. Let's try to simplify this with the help of loops!
# The main advantage of doing so is to reduce the amount of code repitions we have in our script, while still preserving the functionality and purpose
# of the code itself.
# There are a few ways we can do loops in Python, either using "while" or "for" syntax. Remember that programming is heavily logic based, and this is very much true
# of loops, many of which will only run while some statement is true! So let's first implement this with a "while" loop. It's syntax is:
#       while <some statement>:
#           <perform some action>
# We can adapt this to our use case as so:

# sides = 4
# while sides > 0:
#     forward(100)
#     left(90)
#     sides -= 1
# done()

# That's better, notice that we do a couple of new things here. First off we declare a new variable "sides" and assign it the value of 4 with "="
# We can then use that variable in a statement to run our loop. Effectively we are saying "while our variable 'sides' is greater than 0, lets repeat these actions".
# Inside our loop we perform our "forward()" and "left()" operations, but also use "-=" to decrease the value of our variable "sides" by 1 every time it loops through.
# This then allows for our logical statement to have an ending and prevents poor Shelly from drawing squares forever!

# But if this method isn't to your liking we can do this with a "for" loop as well! It's syntax is:
#       for <some variable> in <some grouping>:
#           <perform some action>
# Notice this loop handles variable declaration for us and might further reduce how complex our code is, so lets give it a try!
# We will use "x" as our variable (but it can be anything) and we will use Python's "range()" function to determing how many times we loop!

# for x in range(4):
#     forward(100)
#     left(90)
# done()

# At this time lets talk about a few things regarding our code. First off notice that when we use "left()" or "right()" we are using
# 90 as our value, this is because Shelly rotates in angles and moves "forward" in units! This is an interesting insight and allows us to write code in various
# ways. In our loops we did everything with the number of sides in mind, and didn't really care about our rotations, but what if we factor that in as well! This would allow
# us to draw much more complex shapes! Below I'll use this insight to draw a 6-sided hexagon, I'll just have to make sure that my new rotation adds up to 360 for the number
# of sides! Luckily 360 / 60 = 6, with no remainder!

# sides = 6
# while sides > 0:
#     forward(100)
#     left(60)
#     sides -= 1
# done()

# Lets dive a bit deeper. What if we wanted something a bit rounder, like a circle? "But a circle doesn't have any sides" you might be thinking, and I would say you are correct.
# But what if we made our shape have a large number of sides, and very small rotations, effectively we would be drawing a circular shape! Since we don't know how many sides we will
# need to make it appear like a circle, lets rely just on degrees. Here I am going to move forward a small amount of units, say, 10, and rotate left a small amount as well, say 5.
# My logical condition will be based on the fact that you can only rotate 360 degrees without making a full circle, so every time I loop, I'll decrease my remaining amount of
# degrees by the amount I rotated (5). So lets see how it works:

# degrees = 360
# while degrees > 0:
#     forward(10)
#     left(5)
#     degrees -= 5
# done()

# What if we want to draw multiple shapes? If we were using paper we would just move our pen off the paper and drop is somewhere else. We can do a similar thing here!
# Using the "penup()" and "pendown()" functions we can move our turtle up and down on the paper! Lets draw a circle in one location and a circle in another using some of 
# the turtle module's prebuild shapes. We will also use the "fillcolor("color")", "begin_fill()", and "end_fill()" functions to color them in!

# fillcolor("red")
# begin_fill()
# circle(30)
# end_fill()
# penup()

# forward(100)

# pendown()
# fillcolor("blue")
# begin_fill()
# circle(30)
# end_fill()
# done()

# Previously I mentioned that Shelly moves in units, I wonder if we can do more complex drawings if we use a coordinate system like a graph.
# We can use the "goto(x, y)" function to move our turtle to a specific coordinate.

# goto(20, 20)
# done()

# Shelly moved in a straight line towards the coordinates (20, 20). We didn't have to rotate or do anything else! The center or starting place of our turtle appears to be
# the origin or (0, 0) coordinate. So we tell Shelly to move up 20 units (y), then over another 20 units (x), then to draw a line connecting its new position to its last.
# With that we can plan more complex drawings with graph paper! I'm going to try and draw a small house see below:

goto(0, 20)
goto(10, 30)
goto(20, 20)
goto(20, 0)
goto(0, 0) # return to origin
done()

# We learned a lot in a not so long amount of time! Lets try playing around with what we learned and try to draw some interesting things with the help of our turtle!
























