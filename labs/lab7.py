# lab 7 turtle and shapley testing
# Connor Clark 3/21/2022

import turtle as tur
import shapely as sh


def turtle():
    canvas = tur.Screen()
    canvas.setup(500, 500)
    t = tur.Turtle()
    t.color("black")
    t.circle(100)
    t.goto(0, -50)
    t.color("red")
    t.pendown()
    t.write("Circle")
    canvas.exitonclick()


def shapely():
    pass


turtle()
