from turtle import *
pencolor('red')
fillcolor('yellow')

begin_fill()
points=5

for i in range(points):
    fd(100)
    rt(180-180/points)
end_fill()


points2=7
pu()
setpos(150,0)
pd()
begin_fill()
for i in range(points2):
    forward(100)
    right(180-180/points2)
end_fill()

points3=9
pu()
setpos(0,150)
pd()
begin_fill()
for i in range(points3):
    forward(100)
    right(180-180/points3)
end_fill()

points4=11
pu()
setpos(150,150)
pd()
begin_fill()
for i in range(points4):
    forward(100)
    right(180-180/points4)
end_fill()