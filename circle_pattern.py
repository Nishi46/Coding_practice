from turtle import *
import math
# using the python package turtle


def circle_turtle(radius):
    circle(radius)
    hideturtle()
    done()

# without using the python pacakge turtle shell


def circle_pattern(radius):
    for i in range((2 * radius)+1):
        for j in range((2*radius)+1):
            distance = math.sqrt((i-radius)**2 + (j-radius)**2)
            if(distance > radius - .5 and distance < radius + 0.5):
                print("*", end="")
            else:
                print(" ", end="")
        print()


# uncomment which version you want to run and can change the radius
# circle_turtle(10)
# circle_pattern(10)
