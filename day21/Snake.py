from turtle import Turtle,Screen
import time
from food import Food

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)] #as a global constant at the top
MOVE_DISTANCE =20
DIRECTIONS = {
 "Up" : 90,
 "Down" : 270,
 "Left" : 180,
 "Right" : 0
}
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.segments) -1,0,-1):
            x_new = self.segments[seg_num-1].xcor()
            y_new = self.segments[seg_num-1].ycor()
            new_position = (x_new,y_new)
            self.segments[seg_num].penup()
            self.segments[seg_num].goto(new_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["Down"]:
            self.head.setheading(DIRECTIONS["Up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["Up"]:
            self.head.setheading(DIRECTIONS["Down"])

    def right(self):
        if self.head.heading() != DIRECTIONS["Left"]:
            self.head.setheading(DIRECTIONS["Right"])

    def left(self):
        if self.head.heading() != DIRECTIONS["Right"]:
            self.head.setheading(DIRECTIONS["Left"])

    def add_segment(self):
        new_position = self.segments[-1].position()
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(new_position)
        self.segments.append(new_segment)
        

    def eat_food(self,food):
        if self.head.distance(food) <15:
            food.refresh_food()
            print("nom nom nom")
            self.add_segment()


    def check_collision_with_tail(self):
        for i in range(1,len(self.segments),1):
            if self.head.distance(self.segments[i]) < 15:
                return True