from math import sin, pi

white = [[0 for _1 in range(8)] for _ in range(8)]
black = [[0 for _1 in range(8)] for _ in range(8)]

for y in range(8):
    for x in range(8):
        ranks_w = -1/7 * y + 1
        ranks_b = 1/7 * y

        files = (2/49) * (x - 3.5)**2 + 0.5

        # creates two peaks at the b and g files, since the exact corner is less favorable
        sin_amplitude = 5 # lower is steeper
        files_sin = 1/sin_amplitude * sin(x * pi/2.5 + 0.1 * pi) + (sin_amplitude - 1)/sin_amplitude

        # only use the formula with b/g peaks on the starting file for each color
        if y == 0:
            white[y][x] = (ranks_w + files_sin) / 2
            black[y][x] = (ranks_b + files) / 2

        elif y == 7:
            white[y][x] = (ranks_w + files) / 2
            black[y][x] = (ranks_b + files_sin) / 2

        else:
            white[y][x] = (ranks_w + files) / 2
            black[y][x] = (ranks_b + files) / 2

"""
import matplotlib.pyplot as plt

# plt.plot()

fig, ax = plt.subplots()

ax.imshow(white, cmap=plt.cm.coolwarm, interpolation='nearest')
# im_b = ax.imshow(black, cmap='afmhot', interpolation='nearest')

for i in range(8):
    for j in range(8):
        text = str(round(white[i][j], 3))
        text = ax.text(j, i, text[1:] if text.startswith('0') else text,
                       ha="center", va="center", color="black")

ax.set_xticklabels(['', '0: a', '1: b', '2: c', '3: d', '4: e', '5: f', '6: g', '7: h'])
ax.set_yticklabels(['', '0 (1)', '1 (2)', '2 (3)', '3 (4)', '4 (5)', '5 (6)', '6 (7)', '7 (8)'])

plt.gca().invert_yaxis()
plt.show()
"""