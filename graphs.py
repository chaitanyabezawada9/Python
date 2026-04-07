from turtle import *
import colorsys
speed(0)
pensize(3)
bgcolor('black')
tracer(300)
h = 0
up()
goto(50, -150)
down()
for i in range(500):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005
    fillcolor(col)
    up()
    circle(i, 45)
    down()
    begin_fill()
    circle(90, 145)
    left(80)
    circle(90, 145)
    end_fill()
done()  