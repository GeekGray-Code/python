import turtle
from turtle import *

color('black','')

begin_fill()

for i in range(4):

    fd(200)
    rt(90)

rt(90)
turtle.circle(100,180)
rt(-90)
turtle.circle(100,180)
rt(270)
turtle.circle(100,180)
rt(-90)
turtle.circle(100,180)


end_fill()
done()