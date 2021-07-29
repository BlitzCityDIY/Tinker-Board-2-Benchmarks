import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Tinker Board", "Tinker Board 2", "Raspberry Pi 4, 8GB"]
nums = [338.128437, 466.79351, 443.217292]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Multi-Core Test (Phoronix - himeno, higher is better)")
plt.xlabel("Boards")
plt.ylabel("mflops")
plt.show()