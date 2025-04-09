import turtle

# Setup screen
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("Blue")
screen.setup(width=800, height=600)
screen.tracer(0)  # turn off automatic animation

# Paddle 1 (Left)
paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.color('white')
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2 (Right)
paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.color('white')
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(40)
ball.dx = 0.2
ball.dy = 0.2

# Score
score_1 = 0
score_2 = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        paddle_1.sety(y + 20)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        paddle_1.sety(y - 20)

def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        paddle_2.sety(y + 20)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        paddle_2.sety(y - 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom wall bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball goes past right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        score_display.clear()
        score_display.write(f"Player A: {score_1}  Player B: {score_2}", align="center", font=("Courier", 24, "normal"))

    # Ball goes past left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        score_display.clear()
        score_display.write(f"Player A: {score_1}  Player B: {score_2}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
