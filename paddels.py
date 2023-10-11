
from turtle import Turtle

class Paddel(Turtle):

    def paddle(self,x,y):
            self.color("white")
            self.penup()
            self.shape("square")
            self.goto(x,y)
            self.shapesize(stretch_wid=5, stretch_len=1)


    def up(self):
        new_y= self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


