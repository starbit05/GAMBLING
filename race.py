import turtle
import random

s = turtle.Screen()
s.bgcolor("black")

bob = turtle.Turtle()
jef = turtle.Turtle()


bob.fillcolor("blue")
jef.fillcolor("green")

bob.penup()
jef.penup()

jef.goto(-200,100)
bob.goto(-200,-100)

jef.goto(300,60)
bob.goto(300,-140)

bob.pendown()
jef.pendown()
jef.pencolor("blue")
bob.pencolor("green")

jef.circle(40)
bob.circle(40)

bob.penup()
jef.penup()

jef.goto(-200,100)
bob.goto(-200,-100)

m1 = 0
m2 = 0
while jef.pos() < (300,100) and bob.pos() < (300,-100):
    print("P1 turn")

    m1 = int(input("add money, P1 add"))
    d1 = random.randint(1,6)
    if d1 >= 3 :
        print(d1,"times the money in distance")
        jef.forward(d1*m1)
    else:
        print("nope")
        m1 /= 2

    print("P2 turn")

    m2 = int(input("add money, P2 add"))
    d2 = random.randint(1,6)
    if d2 >= 3:
        print(d2, "times the money in distance")
        bob.forward(d2 * m1)
    else:
        print("nope")
        m2 /= 2
ref = turtle.Turtle()
if jef.pos() > (300, 100):
    print("P1 WINS")
    ref.write("P1 WINS")
else:
    print("P2 WINS")
    ref.write("P2 WINS")

turtle.done()