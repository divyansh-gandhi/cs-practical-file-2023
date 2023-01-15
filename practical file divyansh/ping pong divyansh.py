# ping pong game
# divyansh ganghi
import turtle
import os

wn=turtle.Screen()
wn.title('ping pong bye divyansh')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


#paddle1
p1=turtle.Turtle()
p1.speed(0)#speed of updation
p1.shape('square')
p1.color('white')
p1.shapesize(stretch_wid=5,stretch_len=1)
p1.penup()
p1.goto(-350,0)

#paddle2
p2=turtle.Turtle()
p2.speed(0)#speed of updation
p2.shape('square')
p2.color('white')
p2.shapesize(stretch_wid=5,stretch_len=1)
p2.penup()
p2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)#speed of updation
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
def paddle1_up():
    y=p1.ycor()#it returns the  current y coordinate of the ball
    y+=20
    p1.sety(y)

def paddle1_down():
    y=p1.ycor()#it returns the current y coordinate of the ball
    y-=20
    p1.sety(y)
def paddle2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def paddle2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)
    #keboard binding
wn.listen()
wn.onkeypress(paddle1_up(),'w')
wn.onkeypress(paddle1_down(),'s')
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
     
