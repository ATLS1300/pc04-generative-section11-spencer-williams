"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Spencer Williams

********* HEY, READ THIS FIRST **********

My code will start at the top right of the panel and make a square with random pen width 
size and a random color (from a list I made) as the pen color. It will then move to the
bottom left of the screen and do the same thing. Then, it will move to the top left of 
the screen and make circles  with a randomized radius and a random fill color from the same
list as the squares. It will then repeat the random circle pattern in the bottom right of 
the screen.

"""
import turtle
import math, random

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================


listcolor = ["red", "blue", "green", "yellow", "purple", "brown", "black", "pink"]

square=turtle.Turtle(visible=False) #hides the turtle and renames it
supersq=turtle.Turtle(visible=False) #hides the turtle and renames it
c=turtle.Turtle(visible=False) #hides the tturtle and renames it
new=turtle.Turtle(visible=False)


square.up()
square.goto(50,200)
square.pensize(20)
square.down()
for i in range (4): #for loop for a square
    square.pensize(random.randint(1,30)*5) # gives the pensize a randomized width
    square.pencolor(listcolor[i]) 
    square.pencolor(random.choice(listcolor)) #gives the pencolor a random color
    square.forward(200)
    square.right(90)
    
    

supersq.up()
supersq.goto(-200,-50)
supersq.down()
for t in range (4):  #for loop for a square
    supersq.pensize(random.randint(1,30)*5) #gives the pensize a randomized width
    supersq.pencolor(listcolor[t])
    supersq.pencolor(random.choice(listcolor)) #gives the pencolor a random color
    supersq.forward(200)
    supersq.right(90)
    
c.up()
c.goto(-200,200)
c.down()
for f in range (8): #for loop for circles
    c.begin_fill() #starts a fill
    c.color(listcolor[f])
    c.color(random.choice(listcolor)) #makes the fill color a random color
    c.circle(random.randint(10,50)*3) #makes the radius a random number
    c.end_fill()
    c.right(90)
    c.up()
    c.forward(20)
    c.down()
    
c.up()
c.goto(200,-200)
c.down()
for l in range (8): #for loop for circles
    c.begin_fill()# starts a fill
    c.color(listcolor[f])
    c.color(random.choice(listcolor)) #makes the fill color a random color
    c.circle(random.randint(10,50)*3) #makes the radius a random color
    c.end_fill()
    c.right(90)
    c.up()
    c.forward(20)
    c.down()
    

    

    
    