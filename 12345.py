import math
import random


class Ball:
    x_pos = 15
    y_pos = 3  # 0 = top
    x_vel = 0
    y_vel = 0
    mass = 1
    bounciness = 0.6
    friction = 1.2
    char = "O"

    def __init__(self):
        self.x_vel = random.random() * 6 - 3
        self.y_vel = random.random() * 6 - 3

    def apply_force(self, force_x, force_y):
        self.x_vel = force_x * (1 / self.mass)
        self.y_vel = force_y * (1 / self.mass)

    def simulate(self):
        window[int(self.y_pos)][int(self.x_pos)] = " "

        self.x_pos += self.x_vel
        self.y_vel += gravity * self.mass  # positive velocity = falling
        self.y_pos += self.y_vel
        self.check_bounds()

        window[int(self.y_pos)][int(self.x_pos)] = self.char

    def check_bounds(self):
        if self.x_pos < 0:
            self.x_pos = 0
            self.x_vel = -1 * self.x_vel * self.bounciness
        elif self.x_pos >= window_width:
            self.x_pos = window_width - 1
            self.x_vel = -1 * self.x_vel * self.bounciness

        if self.y_pos >= window_height:
            # Ball hit floor
            self.y_pos = window_height - 1
            self.y_vel = -1 * math.fabs(self.y_vel) * self.bounciness
            if self.y_vel > -gravity * 15:
                self.y_vel = 0
            self.x_vel /= self.friction
        elif self.y_pos < 0:
            # Ball hit ceiling
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
for x in range(ball_count):
    balls.append(Ball())

while True:
    window = [[" " for x in range(window_width)] for y in range(window_height)]  # Resets window
    for ball in balls:
        ball.simulate()
    draw_window()

    input("Enter for next tick")
