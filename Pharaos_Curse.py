
class Particle:
    x_pos = 0
    y_pos = 0
    # Moves:
    # 7 8 9
    # 6 5 4
    # 1 2 3
    moves = []
    x_steps = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    y_steps = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    char = "#"

    def __init__(self, _char):
        self.x_pos = cursor_x
        self.y_pos = cursor_y
        self.char = _char
        if self.char == "#":
            self.moves = [2, 1, 3]
        elif self.char == "O":
            self.moves = [2, 1, 3, 6, 4]

    def simulate(self):
        for move in self.moves:
            if self.move(self.x_steps[move - 1], self.y_steps[move - 1]):
                break
        window[self.y_pos][self.x_pos] = self.char

    def move(self, x, y):
        if window[self.y_pos + y][self.x_pos + x] != " " or self.is_out_of_bounds(self.x_pos + x, self.y_pos + y):
            return False

        window[self.y_pos][self.x_pos] = " "
        self.x_pos += x
        self.y_pos += y

        window[self.y_pos][self.x_pos] = self.char
        return True

    @staticmethod
    def is_out_of_bounds(x, y):
        return x < 0 or x >= window_width - 1 or y < 0 or y >= window_height - 1


def draw_window():
    print("-" * (window_width + 2))
    for y in range(window_height):
        line = "|"
        for x in range(window_width):
            if x == cursor_x and y == cursor_y:
                line += "X"
            else:
                line += window[y][x]
        print(line + "|")
    print("-" * (window_width + 2))


window_width = 35
window_height = 8
window = [[" " for x in range(window_width)] for y in range(window_height)]  # Resets window
cursor_x = int(window_width / 2)
cursor_y = int(window_height / 2)
tick_speed = 5  # x frames between the ticks
toggled_place = False

particles = []
current_particle = "#"
while True:
    for particle in particles:
        particle.simulate()
    draw_window()

    action = input("Enter: Next tick | WASD/M: Move cursor | P/T(toggle): Place(" + current_particle + ") "
            "| C: Switch particle").upper()
    if action == "M":
        move_by = input("x y: ")
        splits = move_by.split(" ")
        cursor_x += int(splits[0])
        cursor_y += int(splits[1])
    elif action == "P":
        particles.append(Particle(current_particle))
    elif action == "T":
        toggled_place = False if toggled_place else True
    elif action == "C":
        selection = input("Sand: #  Water: O  Wall: =")
        current_particle = selection
    elif action == "W":
        cursor_y -= 1
    elif action == "S":
        cursor_y += 1
    elif action == "A":
        cursor_x -= 1
    elif action == "D":
        cursor_x += 1
    elif action == "X":
        break

    if toggled_place:
        particles.append(Particle(current_particle))
