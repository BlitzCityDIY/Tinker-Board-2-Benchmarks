import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["TB, Int", "TB, FP", "TB2, Int", "TB2, FP", "Pi 4, Int", "Pi 4, FP"]
     
nums = [3560.92, 3136.43, 4999.04, 5292.24, 3878.41, 3811.68]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("RAM Test (Phoronix, ramspeed (average, higher is better))")
plt.xlabel("Boards")
plt.ylabel("mb/s")
plt.show()