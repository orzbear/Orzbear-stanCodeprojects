"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause

import extensiongraphics
from extensiongraphics import ExtensionGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage

FRAME_RATE = 20  # 100 frames per second
NUM_LIVES = 4  # Number of attempts


def main():
    graphics = ExtensionGraphics()
    # Define the counting the lives left and the bricks left
    # Live counts labels
    lives = 0
    img = GImage("trump.jpg")
    lives_symbol = img
    # Score board
    bricks_left = int(graphics.brick_rows * graphics.brick_cols)
    bricks_count = bricks_left
    score_board = GLabel(f'Mexican Wall: {bricks_count}%')
    score_board.font = 'Courier-15-bold'
    graphics.window.add(score_board, x=1, y=graphics.window.height - 10)
    # Add the animation loop here!
    while True:
        # Make the ball move
        old_bricks_count = bricks_count
        old_lives = lives
        ball_dx = graphics.get_dx()
        ball_dy = graphics.get_dy()
        graphics.ball.move(ball_dx, ball_dy)
        # Make the ball bounce while touch the wall
        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            graphics.set_dx()
        if graphics.ball.y <= 0:
            graphics.set_dy()
        # If the ball touch the bottom of the window, the ball should be back to the start and stopped till the next
        # click.
        if graphics.ball.y >= graphics.paddle.y+graphics.paddle.height:
            lives += 1
            graphics.ball.x = graphics.ball_start_x
            graphics.ball.y = graphics.ball_start_y
            graphics.set_start()
        # Make the ball bounce while touching the paddle and the bricks
        x1 = graphics.ball.x
        x2 = graphics.ball.x + 2 * graphics.ball_radius
        y1 = graphics.ball.y
        y2 = graphics.ball.y + 2 * graphics.ball_radius
        if graphics.window.get_object_at(x1, y1) is not None:
            o = graphics.window.get_object_at(x1, y1)
            # If the ball touched the paddle, it should bounce.
            if o is graphics.paddle:
                # Avoiding the ball stuck in the paddle
                # If the bounce can make the ball out of the paddle, bounce the ball
                if y2 - ball_dy < graphics.paddle.y:
                    graphics.set_dy()
                # if not, only change the direction once, and then move till it leaves the paddle.
                else:
                    if ball_dy > 0:
                        # If dy <0, means it no longer need to change direction
                        graphics.set_dy()
            elif o is not graphics.paddle and o is not score_board and o is not lives_symbol:
                # If it is a brick, remove it and then bounce.
                graphics.set_dy()
                graphics.window.remove(o)
                bricks_count -= 1
        #  Repeat it in all four point of the square
        elif graphics.window.get_object_at(x1, y2) is not None:
            o = graphics.window.get_object_at(x1, y2)
            if o is graphics.paddle:
                if y2 - ball_dy < graphics.paddle.y:
                    graphics.set_dy()
                else:
                    if ball_dy > 0:
                        graphics.set_dy()
            elif o is not graphics.paddle and o is not score_board and o is not lives_symbol:
                graphics.set_dy()
                graphics.window.remove(o)
                bricks_count -= 1
        elif graphics.window.get_object_at(x2, y1) is not None:
            o = graphics.window.get_object_at(x2, y1)
            if o is not None:
                if o is graphics.paddle:
                    if y2 - ball_dy < graphics.paddle.y:
                        graphics.set_dy()
                    else:
                        if ball_dy > 0:
                            graphics.set_dy()
                elif o is not graphics.paddle and o is not score_board and o is not lives_symbol:
                    graphics.set_dy()
                    graphics.window.remove(o)
                    bricks_count -= 1
        elif graphics.window.get_object_at(x2, y2) is not None:
            o = graphics.window.get_object_at(x2, y2)
            if o is not None:
                if o is graphics.paddle:
                    if y2 - ball_dy < graphics.paddle.y:
                        graphics.set_dy()
                    else:
                        if ball_dy > 0:
                            graphics.set_dy()
                elif o is not graphics.paddle and o is not score_board and o is not lives_symbol:
                    graphics.set_dy()
                    graphics.window.remove(o)
                    bricks_count -= 1
        #  Renew score
        if old_bricks_count != bricks_count:
            graphics.window.remove(score_board)
            score_board = GLabel(f'Mexican Wall: {bricks_count}%')
            score_board.font = 'Courier-15-bold'
            graphics.window.add(score_board, x=1, y=graphics.window.height - 10)
        #  Renew lives
        if old_lives != lives:
            for i in range(lives+1):
                img = GImage("trump.jpg")
                lives_symbol = img
                graphics.window.add(lives_symbol, x=graphics.window.width - i*img.width,
                                    y=graphics.window.height - img.height)
        #  Pausing
        pause(FRAME_RATE)
        if lives == NUM_LIVES or bricks_count == 0:
            # If the lives left is 0 or there are no more bricks, the game should end.
            break
    # If the game has been ended, the ball back to the start and clicked will not make it move.
    if lives == NUM_LIVES:
        graphics.ball.x = graphics.ball_start_x
        graphics.ball.y = graphics.ball_start_y
        graphics.set_start()
        end = GImage("trump_end.jpg")
        graphics.window.add(end, x=(graphics.window.width-end.width)/2,
                            y=(graphics.window.height-end.height)/2-36)
        dead1 = GLabel("Congrats!")
        dead1.color = 'red'
        dead1.font = 'Courier-18-bold-italic'
        graphics.window.add(dead1, x=(graphics.window.width-dead1.width)/2,
                            y=(graphics.window.height-dead1.height)/2-36)
        dead2 = GLabel("You make America great again!")
        dead2.color = 'red'
        dead2.font = 'Courier-18-bold-italic'
        graphics.window.add(dead2, x=(graphics.window.width-dead2.width)/2, y=(graphics.window.height-dead2.height)/2)
    elif bricks_count == 0:
        graphics.ball.x = graphics.ball_start_x
        graphics.ball.y = graphics.ball_start_y
        graphics.set_start()
        end = GImage("trump_sad.jpg")
        graphics.window.add(end, x=(graphics.window.width-end.width)/2,
                            y=(graphics.window.height-end.height)/2-36)
        dead1 = GLabel("Oops!")
        dead1.color = 'red'
        dead1.font = 'Courier-18-bold-italic'
        graphics.window.add(dead1, x=(graphics.window.width-dead1.width)/2,
                            y=(graphics.window.height-dead1.height)/2-36)
        dead2 = GLabel("See you 2024!")
        dead2.color = 'red'
        dead2.font = 'Courier-18-bold-italic'
        graphics.window.add(dead2, x=(graphics.window.width-dead2.width)/2, y=(graphics.window.height-dead2.height)/2)


if __name__ == '__main__':
    main()
