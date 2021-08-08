"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    lives = NUM_LIVES

    while True:
        if lives > 0:
            # pause
            pause(FRAME_RATE)
            if graphics.click_off:
                graphics.ball.move(dx, dy)
                # Ball bounce against the wall
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    dx = -dx
                if graphics.ball.y <= 0 or graphics.ball.y >= graphics.window.height - graphics.ball.height:
                    dy = -dy
                # Ball rebound if touch obj
                if graphics.check_ball_collisions() == 'rebound':
                    dy = -dy
                # over paddle, ball can not rebound and also live -1
                if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                    graphics.window.remove(graphics.ball)
                    lives -= 1
                    graphics.click_off = False
                    # back to start position
                    graphics.restart_ball()
                # all bricks remove
                if graphics.brick_count == graphics.brick_cols * graphics.brick_rows:
                    break
        else:
            break







if __name__ == '__main__':
    main()
