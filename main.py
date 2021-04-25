import turtle
from player import Player
from block import Block

START_PLAYER_POSITION = (0, -250)

# setup the main screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Breakout")

# setup the player bar
player = Player(START_PLAYER_POSITION)

# setup the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")

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

screen.exitonclick()
