import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["TB, 1 Thread", "TB, 2 Threads", "TB, 4 Threads", "TB, 8 Threads",
"TB 2, 1 Thread", "TB 2, 2 Threads", "TB 2, 4 Threads", "TB 2, 8 Threads", 
"Pi 4, 1 Thread", "Pi 4, 2 Threads", "Pi 4, 4 Threads", "Pi 4, 8 Threads"]
nums = [29.43, 56.493, 126.688, 265.369,
        32.61, 54.301, 114.762, 186.798,
        60.653, 116.436, 228.233, 454.41]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Linux Kernel Scheduler - Threads (Phoronix, Hackbench - lower is better)")
plt.xlabel("Boards")
plt.ylabel("Seconds")
plt.show()