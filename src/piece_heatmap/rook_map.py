white = [[0 for _1 in range(8)] for _ in range(8)]
black = [[0 for _1 in range(8)] for _ in range(8)]

for y in range(8):
    for x in range(8):
        rank_w = 2 ** (y - 5.43) if y < 6 else -0.25 * (y - 6) ** 2 + 1.5
        rank_b = (1/2) ** (y - 1.57) if y > 1 else -0.25 * (y - 1) ** 2 + 1.5

        file = -0.05 * (x - 3.5) ** 2 + 1

        white[y][x] = (rank_w + file) / 2
        black[y][x] = (rank_b + file) / 2

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