from turtle import *
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP =90
DOWN = 270
RIGHT =0
LEFT = 180
class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head =self.parts[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        part = Turtle("circle")
        part.color("red")
        part.penup()  # so that it does not create a line
        part.goto(position)
        self.parts.append(part)
    def reset_snake(self):
        for seg in self.parts:
            seg.goto(1000,1000)
        self.parts.clear()
        self.create_snake()
        self.head =self.parts[0]
    def extend(self):
        self.add_segment(self.parts[-1].position())
    def move(self):
        for seg_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[seg_num - 1].xcor()
            new_y = self.parts[seg_num - 1].ycor()
            self.parts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() !=LEFT:
           self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)