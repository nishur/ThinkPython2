import turtle
import math

#1. Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.Write a function call that passes bob as an argument to square, and then run the program again.

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

bob = turtle.Turtle()
#square(bob)

#2. Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for length.

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#for i in range(100, 200, 10):
#    square(bob, i)

#3. Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.  
def polygon(t, len, n):
    for i in range(n):
        t.fd(len)
        t.lt(360/n)
    
#polygon(bob, 50, 6)

# 4 Write a function called circle that takes a turtle,  t, and radius, r, as parameters and that draws an approximate circle by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r. Hint: figure out the circumference of the circle and make sure that length * n = circumference.
def circle(t, r):
    circumferance = 2 * math.pi * r
    length = 10
    n = int(circumferance / length)
    polygon(t, length, n)

#circle(bob, 100)

#Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.  
def 