import turtle
from player import Player
from block import Block
from ball import Ball

# setup the main screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Breakout")

# setup the player bar
player = Player()

# setup the ball
ball = Ball()

blocks = []
#setup the blocks to destroy
for b in range(10):
    for row in range(4):
        block = Block(b, row)
        blocks.append(block)

# Check for player movement
screen.listen()
screen.onkeypress(player.go_left,"Left")
screen.onkeypress(player.go_right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    #Detect collision with player
    if ball.distance(player) < 15:
        ball.bounce_ball()

screen.exitonclick()
