import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Tinker Board", "Tinker Board 2", "Raspberry Pi 4, 8GB"]
     
nums = [17.659, 22.37, 26.026]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Jetstream 2.0 (Javascript Browser Performance (higher is better))")
plt.xlabel("Boards")
plt.ylabel("Score")
plt.show()