import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from presets import apply_publication_style, export_figure

x = np.arange(5)
a = np.array([0.42, 0.55, 0.63, 0.69, 0.73])
b = np.array([0.39, 0.51, 0.60, 0.66, 0.70])

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.plot(x, a, marker="o", label="Model A")
ax.plot(x, b, marker="s", label="Model B")
ax.set_title("Performance Comparison")
ax.set_xlabel("Training round")
ax.set_ylabel("Score")
ax.legend()
fig.savefig("before.png", dpi=150, bbox_inches="tight")
plt.close(fig)

w, h = apply_publication_style("single-column")
fig, ax = plt.subplots(figsize=(w, h))
ax.plot(x, a, marker="o", label="Model A")
ax.plot(x, b, marker="s", linestyle="--", label="Model B")
ax.set_xlabel("Training round")
ax.set_ylabel("Score")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(frameon=False, loc="lower right")
ax.margins(x=0.03)
fig.tight_layout(pad=0.4)
export_figure(fig, "after")
plt.close(fig)
