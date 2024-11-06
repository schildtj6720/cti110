# Jasmine Schildt
# 11/5/2024
# P4LAB1
# A program with a turtle graphics programs that draws a triangle and a square using loops.

import turtle

for i in range(4):
    turtle.forward(50)
    turtle.right(90)

turtle.penup()
turtle.forward(100)
turtle.pendown()

for i in range(3):
    turtle.forward(50)
    turtle.right(120)

