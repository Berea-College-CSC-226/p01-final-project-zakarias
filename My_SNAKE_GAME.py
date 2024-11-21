import turtle

class SnakeGame:
     def __init__(self):
        wn = turtle.Screen()  #Screen setup
        wn.title("The Snake Game")
        wn.bgcolor("green")
        wn.setup(width=500, height= 500)

        #Snake head
        head = turtle.Turtle()
        head.speed(0)
        head.shape("circle")
        head.color("blue")
        head.penup()
        head.goto(0,0)




        #Snake food


        wn.mainloop()


Game = SnakeGame()









