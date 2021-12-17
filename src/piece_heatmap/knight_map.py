white = [[0 for _1 in range(8)] for _ in range(8)]
black = [[0 for _1 in range(8)] for _ in range(8)]

for y in range(8):
    for x in range(8):
        ranks = max(-1 * abs(0.125 * (x - 4)) + 1, -1 * abs(0.125 * (x - 3)) + 1)
        files = max(-1 * abs(0.125 * (y - 4)) + 1, -1 * abs(0.125 * (y - 3)) + 1)

        white[y][x] = (ranks + files) / 2

black = white

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