import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("bar.png", 0.3)
        self.__status = False
        self.change_x = 3

    def update(self):

        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        elif self.left <= 0:
            self.left = 0

        if self.is_active():
            self.center_x += self.change_x

    def is_active(self):
        return self.__status

    def activate(self):
        self.__status = True


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 0.2)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left <= 0:
            self.change_x = -self.change_x
        elif self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x

        if self.bottom <= 0:
            self.change_y = -self.change_y
        elif self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y


class PingPong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.score_camera = None
        self.score = 0
        self.setup()

    def setup(self):
        # Start position of the bar
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 9
        # Start position of the ball
        self.ball.center_x = SCREEN_WIDTH / 3
        self.ball.center_y = SCREEN_HEIGHT / 3

    def update(self, delta_time: float):
        self.ball.update()
        self.bar.update()
        # Check if the ball hit the bar
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = -self.ball.change_y

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bar.change_x = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 3

        elif key == arcade.key.LEFT:
            self.bar.change_x = -3

        self.bar.activate()


if __name__ == '__main__':
    window = PingPong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()