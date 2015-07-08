import turtle
import random
import colorsys

def tree(branchLen, thickness,t):
    if branchLen > 1 and branchLen > 1:
        h = random.uniform(0.25, 0.38) # Select random green'ish hue from hue wheel
        s = random.uniform(0.2, 1)
        v = random.uniform(0.3, 1)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        t.pencolor((r, g, b))
        t.width(thickness)
        t.forward(branchLen)
        randomAngle = random.randint(20,30)
        t.right(randomAngle)
        tree(branchLen-random.randint(5,10), thickness-1,t)
        t.left(2*randomAngle)
        tree(branchLen-random.randint(5,10), thickness-1,t)
        t.right(randomAngle)
        t.up()
        t.backward(branchLen)
        t.down()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, 15,t)
    myWin.exitonclick()

main()
