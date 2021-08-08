"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

it's a simple called breakout, good luck!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.r = ball_radius
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_count = 0  # equal to score

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-(paddle_offset+paddle_height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-self.ball.width)/2,y=(window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.set_ball_velocity()

        # Initialize our mouse listeners
        self.click_off = False
        onmouseclicked(self.release_ball)    # click and start the game release the ball
        onmousemoved(self.paddle_move)

        # arrange bricks
        for i in range(0, window_width, brick_width+brick_spacing):
            for j in range(brick_offset, brick_offset+(brick_height+brick_spacing)*(brick_cols//5), brick_height+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.window.add(self.brick, x=i, y=j)
        for i in range(0, window_width, brick_width+brick_spacing):
            for j in range(brick_offset+(brick_height+brick_spacing)*(brick_cols//5),brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*2, brick_height+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'orange'
                self.window.add(self.brick, x=i, y=j)
        for i in range(0, window_width, brick_width+brick_spacing):
            for j in range(brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*2, brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*3, brick_height+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                self.window.add(self.brick, x=i, y=j)
        for i in range(0, window_width, brick_width+brick_spacing):
            for j in range(brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*3, brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*4, brick_height+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'green'
                self.window.add(self.brick, x=i, y=j)
        for i in range(0, window_width, brick_width+brick_spacing):
            for j in range(brick_offset+(brick_height+brick_spacing)*(brick_cols//5)*4, brick_offset+(brick_height+brick_spacing)*brick_cols, brick_height+brick_spacing):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i, y=j)

    def release_ball(self, m):
        self.click_off = True

    def paddle_move(self, m):
        self.paddle.x = m.x-self.paddle.width/2
        if m.x <= self.paddle.width/2:
            # the left limit
            self.paddle.x = 0
        if m.x >= self.window.width-(self.paddle.width/2):
            # the right limit
            self.paddle.x = self.window.width-self.paddle.width

    def set_ball_velocity(self):
        # random speed at x and
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def check_ball_collisions(self):
        a = self.window.get_object_at(self.ball.x, self.ball.y)
        b = self.window.get_object_at(self.ball.x+self.r*2, self. ball.y)
        c = self.window.get_object_at(self.ball.x+self.r*2, self.ball.y+self.r*2)
        d = self.window.get_object_at(self.ball.x, self.ball.y+self.r*2)
        if a is not None:
            if a is not self.paddle:
                # if is brick than remove brick
                self.window.remove(a)
                self.brick_count += 1
            # both bricks and paddle need rebound
            return 'rebound'
        if b is not None:
            if b is not self.paddle:
                # if is brick than remove brick
                self.window.remove(b)
                self.brick_count += 1
            # both bricks and paddle need rebound
            return 'rebound'
        if c is not None:
            if c is not self.paddle:
                # if is brick than remove brick
                self.window.remove(c)
                self.brick_count += 1
            # both bricks and paddle need rebound
            return 'rebound'
        if d is not None:
            if d is not self.paddle:
                # if is brick than remove brick
                self.window.remove(d)
                self.brick_count += 1
            # both bricks and paddle need rebound
            return 'rebound'

    def restart_ball(self):
        self.ball = GOval(self.r * 2, self.r * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)






























