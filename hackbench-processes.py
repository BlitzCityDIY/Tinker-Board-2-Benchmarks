import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["TB, 1 Process", "TB, 2 Processes", "TB, 4 Processes", "TB, 8 Processes",
"TB 2, 1 Process", "TB 2, 2 Processes", "TB 2, 4 Processes", "TB 2, 8 Processes", 
"Pi 4, 1 Process", "Pi 4, 2 Processes", "Pi 4, 4 Processes", "Pi 4, 8 Processes"]
nums = [29.881, 57.301, 125.229, 269.482,
        32.025, 44.05, 87.559, 177.644,
        58.219, 111.543, 220.323, 438.54]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Linux Kernel Scheduler - Processes (Phoronix, Hackbench - lower is better)")
plt.xlabel("Boards")
plt.ylabel("Seconds")
plt.show()