import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["TB, TB 2, Pi 4", "Create", "Files",
"TB, TB 2, Pi 4", "Create", "threads", 
"TB, TB 2, Pi 4", "Create", "Processes", 
"TB, TB 2, Pi 4", "Launch", "programs",
"TB, TB 2, Pi 4", "Memory", "allocations"]
     
nums = [394.339855, 299.600187, 421.446667,
43.606758, 56.522687, 80.27633,
94.133218, 152.94075, 218.216578,
309.85297, 393.62669, 612.209638,
396.85297, 394.859632, 184.744596]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("OSBench (Phoronix, lower is better))")
plt.xlabel("Boards")
plt.ylabel("uSeconds")
plt.show()