import turtle
import time
import random

class SnakeGame:
     def __init__(self):
        self.wn = turtle.Screen()  #Screen setup
        self.wn.title("The Snake Game")
        self.wn.bgcolor("#003200")
        self.wn.setup(width=900, height= 500)

        #Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("circle")
        self.head.color("Black")
        self.head.penup()
        self.head.goto(0,0)
        self.head.direction = "stop"

        #Snake food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("brown")
        self.food.penup()
        self.food.goto(0, 100)
        #segment
        self.segments = []
        #score
        self.score = 0
        self. High_score = 0

        #pen for writing score on the board
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("brown")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    #functions
    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}",
                       align="center", font=("Courier", 24, "normal"))





        self.wn.mainloop()
        # Main game loop




Game = SnakeGame()









