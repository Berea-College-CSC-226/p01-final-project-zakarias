import turtle
import time
import random
class SnakeGame:
    def __init__(self):
        # Set up the screen
        self.wn = turtle.Screen()
        self.wn.title("Snake Game")
        self.wn.bgcolor("#003200")
        self.wn.setup(width=800, height=600)

        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(12)
        self.head.shape("circle")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Snake food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("brown")
        self.food.penup()
        self.food.goto(0, 100)

        # Snake body segments
        self.segments = []
        # Score
        self.score = 0
        self.high_score = 0

        # Pen for writing the score
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("grey")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_scoreboard()

        # Keyboard bindings
        self.wn.listen()
        self.wn.onkey(self.go_up, "Up")
        self.wn.onkey(self.go_down, "Down")
        self.wn.onkey(self.go_left, "Left")
        self.wn.onkey(self.go_right, "Right")

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}",
                       align="center", font=("Courier", 20, "normal"))

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"
    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

      #Changing snake's head direction up to 20 unites depending on the direction
    def move(self):
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)

    #Reset the game
    def reset_game(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.score = 0
        self.update_scoreboard()

    def check_collision(self):
        # Checking for borders collision.
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.reset_game()

        # Body collision with itself
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.reset_game()

        #Chech for for collision
    def check_food_collision(self):
        if self.head.distance(self.food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            self.food.goto(x, y)
              #add a new snake body after eating
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("black")
            new_segment.penup()
            self.segments.append(new_segment)
             #Add poits and update the new score
            self.score += 5
            if self.score > self.high_score:
                self.high_score = self.score
            self.update_scoreboard()
    def update_segments(self): # Follow the old body
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
            #Move the first body and Follow the head
        if self.segments:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

    def run_game(self):   #Kichwa ya game, Check if everything is updated.
        while True:
            self.wn.update()
            self.check_collision()
            self.check_food_collision()
            self.update_segments()
            self.move()
            time.sleep(0.15)

if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()