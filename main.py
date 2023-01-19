import turtle as t
import random
t.colormode(255)
def colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_color = (r, g, b)
    return my_color


def forwards():
    tim.color(colors())
    tim.fd(10)


def backward():
    tim.color(colors())
    tim.bk(10)


def counterclockwise():
    tim.color(colors())
    tim.left(10)


def clockwise():
    tim.color(colors())
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim = t.Turtle()

tim.shape("turtle")
screen = t.Screen()

dic_of_functions = {
    forwards : "w" ,
    backward : "s",
    counterclockwise : "a",
    clockwise : "d",
    clear_screen  : "c"
    }



for _ in range(100):
    for i,j in dic_of_functions.items():
        
        screen.listen()
        screen.onkey(fun=i, key = j)
        

screen.exitonclick()
