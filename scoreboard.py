from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
 
# Setup the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
 
# Initialize Game Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()


