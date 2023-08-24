import random
import math

# 2.
print()
totalSeconds = random.randint(1, 10000)
minutes = math.floor(totalSeconds / 60)
print(str(minutes) + " Minuten und " + str(totalSeconds % 60) + " Sekunden")
