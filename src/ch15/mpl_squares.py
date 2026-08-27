import matplotlib.pyplot as plt


outputs = [1, 4, 9, 16, 25]
inputs = [1,2,3,4,5]

fig, ax = plt.subplots()
ax.plot(inputs, outputs, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Value", fontsize=12)

plt.show()