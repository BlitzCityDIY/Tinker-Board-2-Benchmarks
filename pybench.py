import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Tinker Board", "Tinker Board 2", "Raspberry Pi 4, 8GB"]
nums = [9287, 4515, 5228]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Python Benchmark (Phoronix, Pybench - lower is better)")
plt.xlabel("Boards")
plt.ylabel("Milliseconds")
plt.show()