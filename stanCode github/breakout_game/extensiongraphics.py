"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 20     # Height of the paddle (in pixels)
PADDLE_OFFSET = 110     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class ExtensionGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        #  Create the start point of the ball( in the middle of the window)
        self.ball_start_x = (window_width-2*ball_radius)/2
        self.ball_start_y = (window_height-2*ball_radius)/2
        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        for i in range(0, (brick_width+brick_spacing)*brick_rows, (brick_width+brick_spacing)):
            for j in range(brick_offset, brick_offset+(brick_height+brick_spacing)*brick_cols,
                           brick_height+brick_spacing):
                col = ((j-brick_offset) // (brick_height+brick_spacing)) % 10
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if 0 <= col <= 1:
                    self.brick.fill_color = 'red'
                elif 2 <= col <= 3:
                    self.brick.fill_color = 'orange'
                elif 4 <= col <= 5:
                    self.brick.fill_color = 'yellow'
                elif 6 <= col <= 7:
                    self.brick.fill_color = 'green'
                elif 8 <= col <= 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i, y=j)
                if self.brick.x == window_width - brick_width:
                    col += 1

    #  Make the paddle move with the mouse
    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2

    #  Make the ball move after the mouse click
    def ball_move(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED

    #  Get the dx for the users
    def get_dx(self):
        return self.__dx

    #  Get the dx for the users
    def get_dy(self):
        return self.__dy

    # Set the dx to multiply -1
    def set_dx(self):
        self.__dx *= -1

    # Set the dy to multiply -1
    def set_dy(self):
        self.__dy *= -1

    # Make the ball stop moving
    def set_start(self):
        self.__dx = 0
        self.__dy = 0
