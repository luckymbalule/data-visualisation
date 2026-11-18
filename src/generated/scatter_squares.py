import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
OUTPUT_DIR = BASE_DIR / "outputs" / "scatter"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

inputs = range(1, 6)
outputs = [x**3 for x in inputs]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(inputs, outputs, c=outputs, cmap=plt.cm.okabe_ito)

ax.set_title("Cubic Exponential Scatter")
ax.set_ylabel("Exponents")
ax.set_xlabel("Inputs")

plt.savefig(OUTPUT_DIR / "scatter_plot.png")
plt.show()