import turtle
from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

leo.hideturtle()
def move_forwards():
    '''Move the turle forwards'''
    leo.forward(10)

def move_backwards():
    '''Move the turle backwards'''
    leo.backward(10)

def move_counter_clockwise():
    '''Move the turle counter-clock'''
    leo.left(10)

def move_clockwise():
    '''Move the turle clockwise'''
    leo.right(10)

def clear():
    screen.clear()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_counter_clockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()