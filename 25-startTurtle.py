from turtle import *


def starT():
    pencolor('red')
    fillcolor('yellow')
    begin_fill()
    points=5
    for i in range(points):
        delay(50)
        forward(100)
        right(180-180/points)
    end_fill()
penup()
setpos(100,0)
pendown()

starT()
penup()
forward(125)
pendown()
starT()

penup()
setpos(0,100)
pendown() 
starT()
penup()
forward(125)
pendown()
starT()