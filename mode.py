from turtle import Screen, Turtle

menu = Screen()
turtle = Turtle()

class Modes:

    def __init__(self):
        self.menu



        self.mode = screen.textinput("Select your difficulty!", "Easy, Normal, or Hard?")
        self.difficulties = ["Easy", "easy", "Normal", "normal", "Hard", "hard"]
        if self.mode == "Easy" or "easy":
            turtle.speed("slow")

    def jungle(self):
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("green")
        screen.title("Snicky-Snake Game")
        screen.tracer(0)
