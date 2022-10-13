# import colorgram

# colors = colorgram.extract('image.jpg', 84)

# rgb_colors = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147),
              (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]
kaizen = Turtle()
screen = Screen()
number_of_dots = 100
kaizen.speed('fastest')


def start_position():
    kaizen.hideturtle()
    kaizen.penup()
    kaizen.setx(-450)
    kaizen.sety(-370)


screen.colormode(255)
start_position()

for dot_count in range(1, number_of_dots + 1):
    kaizen.dot(20, random.choice(color_list))
    kaizen.forward(50)

    if dot_count % 10 == 0:
        kaizen.setheading(90)
        kaizen.forward(50),
        kaizen.setheading(180)
        kaizen.forward(500)
        kaizen.setheading(0)

screen.exitonclick()
