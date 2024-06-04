from turtle import *

#declare speed for pen

shape('turtle')
width(7)
#wall1
forward(300)
right(90)

#wall2
forward(300)
right(90)

#wall3
forward(300)
right(90)

#wall4
forward(300)


right(60)
forward(175)

penup()
goto(300,0)
pendown()


left(120)
forward(175)

penup()
goto(120,-300)
pendown()

#door leftside
right(60)
forward(100)
#door topside
right(90)
forward(60)
#door rightside
right(90)
forward(100)



#window

penup()
goto(120,-140)
pendown()

#window side1
left(90)
forward(60)
#window side2
left(90)
forward(60)
#window side3
left(90)
forward(60)
#window side4
left(90)
forward(60)

#cross in window
penup()
goto(150,-140)
pendown()

right(180)
forward(60)

penup()
goto(120,-110)
pendown()

right(90)
forward(60)



exitonclick()