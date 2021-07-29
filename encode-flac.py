import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Tinker Board", "Tinker Board 2", "Raspberry Pi 4, 8GB"]
nums = [123.72, 69.45, 110.209]

plt.bar(boards, nums, color = 'artic')
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Single-Core Test (Phoronix - encode-flac, lower is better)")
plt.xlabel("Boards")
plt.ylabel("Seconds")
plt.show()