from turtle import*
import time
from snake2 import Snake
from food import Food
from scoreboard import Scoreboard
screen  = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# creating snake body
   # OR
# turtle1 = Turtle("square")
# turtle1.color("white")
# turtle1.goto(x=0,y=0)
# turtle2 = Turtle("square")
# turtle2.color("white")
# turtle2.goto(x=-20,y=0)
# turtle3 = Turtle("square")
# turtle3.color("white")
# turtle3.goto(x=-40,y=0)

# moving the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
   screen.update()   # when all the pieces have moved then update the screen
   time.sleep(0.1)

   snake.move()

   # detect collision with food
   if snake.head.distance(food) <15:
      food.refresh()
      snake.extend()
      scoreboard.increase_score()


# detect collision with the wall
   if snake.head.xcor() >290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
      # game_is_on=False   , now we are maintaining high score
      # scoreboard.game_over()
      scoreboard.reset()
      snake.reset_snake()

# detect collision with the tail
   for segment in snake.parts[1:]:  # using slicing
      if snake.head.distance(segment) <10:
         scoreboard.reset()
         snake.reset_snake()
# game_is_on =False , now we are maintainig high score .
# scoreboard.game_over()

#        OR

# detect collision with the tail
#    for segment in snake.parts:
#       if segment == snake.head:
#          pass
#       elif snake.head.distance(segment) <10:
#          game_is_on =False
#          scoreboard.game_over()


screen.exitonclick()