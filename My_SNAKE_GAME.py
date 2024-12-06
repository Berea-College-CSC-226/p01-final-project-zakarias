import turtle
import time
import random

class SnakeGame:
     def __init__(self):
        wn = turtle.Screen()  #Screen setup
        wn.title("The Snake Game")
        wn.bgcolor("#003200")
        wn.setup(width=900, height= 500)

        #Snake head
        head = turtle.Turtle()
        head.speed(0)
        head.shape("circle")
        head.color("Black")
        head.penup()
        head.goto(0,0)
        head.direction = "stop"

        #Snake food
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("brown")
        food.penup()
        food.goto(0, 100)
        #segment
        segments = []
        #score
        score = 0
        High_score = 0

        #pen for writing score on the board
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("brown")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
        #functions
        def go_up():
             if head.direction != "Down":
                 head.direction = "Up"
        def go_down():
            if head.direction != "Up":
                head.direction = "Down"

        def go_left():
            if head.direction != "Right":
                head.direction = "Left"

        def go_right():
            if head.direction != "Left":
                head.direction = "Right"

        def move():
            if head.direction == "Up":
                y = head.ycor()
                head.sety(y + 20)

            if head.direction == "Down":
                y = head.ycor()
                head.sety(y - 20)

            if head.direction == "Left":
                x = head.xcor()
                head.setx(x - 20)

            if head.direction == "Right":
                x = head.xcor()
                head.setx(x + 20)

            #Keyboard for Playing the game
            # use different arrows keys to go to opposite direction
            wn.listen()
            wn.onkey(go_right,"Up")
            wn.onkey(go_down, "Down")
            wn.onkey(go_left, "Left")
            wn.onkey(go_right, "Right")

            # Main game loop
            while True:
                wn.update()

                # Check for a collision with the border
                if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"

                    # Hide the segments
                    for segment in segments:
                        segment.goto(1000, 1000)  # Move them off screen

                    # Clear the segments list
                    segments.clear()

                    # Reset the score
                    score = 0
                    pen.clear()
                    pen.write(f"Score: {score}  High Score: {high_score}", align="center",
                              font=("Courier", 24, "normal"))

                # Check for a collision with the food
                if head.distance(food) < 20:
                    # Move the food to a random spot
                    x = random.randint(-290, 290)
                    y = random.randint(-290, 290)
                    food.goto(x, y)

                    # Add a segment to the snake
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("black")
                    new_segment.penup()
                    segments.append(new_segment)

                    # Increase the score
                    score += 5

                    if score > high_score:
                        high_score = score

                    pen.clear()
                    pen.write(f"Score: {score}  High Score: {high_score}", align="center",
                              font=("Courier", 24, "normal"))

                # Move the end segments first in reverse order
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)

                # Move segment 0 to where the head is
                if len(segments) > 0:
                    x = head.xcor()
                    y = head.ycor()
                    segments[0].goto(x, y)

                move()

        wn.mainloop()
        # Main game loop




Game = SnakeGame()









