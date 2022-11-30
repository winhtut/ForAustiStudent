# draw a colourful star
from turtle import *
pencolor('red')
fillcolor('yellow')
begin_fill()
points=5
for i in range(points):
    forward(100)
    right(180-180/points)
end_fill()