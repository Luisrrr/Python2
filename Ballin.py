import math
import random


class Ball:
    x_pos = 0
    y_pos = 0  # 0 = top
    x_vel = 0
    y_vel = 0
    mass = 1
    bounciness = 0.6
    friction = 1.2
    char = "O"
    respawn = False  # Respawns when it is close to static

    def __init__(self, _respawn = False):
        # Spawn at center
        self.x_pos = window_width / 2
        self.y_pos = window_height / 2

        self.apply_force(random.random() * 6 - 3, random.random() * 6 - 3)
        self.respawn = _respawn

    def apply_force(self, force_x, force_y):
        self.x_vel = force_x / self.mass
        self.y_vel = force_y / self.mass

    def simulate(self):
        window[int(self.y_pos)][int(self.x_pos)] = " "

        self.x_pos += self.x_vel
        self.y_vel += gravity * self.mass  # positive velocity = falling
        self.y_pos += self.y_vel
        self.check_bounds()

        window[int(self.y_pos)][int(self.x_pos)] = self.char

    def check_bounds(self):
        if self.x_pos < 0:
            # Hit left wall
            self.x_pos = 0
            self.x_vel = -1 * self.x_vel * self.bounciness
        elif self.x_pos >= window_width:
            # Hit right wall
            self.x_pos = window_width - 1
            self.x_vel = -1 * self.x_vel * self.bounciness

        if self.y_pos >= window_height:
            # Hit floor
            self.y_pos = window_height - 1
            self.y_vel = -1 * math.fabs(self.y_vel) * self.bounciness
            if self.y_vel > -gravity * 15:
                self.y_vel = 0
                if self.respawn and math.fabs(self.x_vel) < 0.2:
                    self.__init__()
            self.x_vel /= self.friction
        elif self.y_pos < 0:
            # Hit ceiling
            self.y_pos = 0
            self.y_vel = math.fabs(self.y_vel)


def draw_window():
    print("-" * (window_width + 2))
    for y in range(window_height):
        line = "|"
        for x in range(window_width):
            line += window[y][x]
        print(line + "|")
    print("-" * (window_width + 2))


window_width = 35
window_height = 8
gravity = 0.01
balls = []
ball_count = 5
spawn_interval = 0  # In frames
for c in range(ball_count):
    balls.append(Ball(False))

frame_counter = 0
while True:
    window = [[" " for x in range(window_width)] for y in range(window_height)]  # Resets window
    for ball in balls:
        ball.simulate()
    draw_window()

    if spawn_interval != 0:
        frame_counter += 1
        if frame_counter >= spawn_interval:
            frame_counter = 0
            balls.append(Ball())
    if input("Enter for next tick") == "x":
        break
