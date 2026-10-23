from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt

PRESETS = {
    "single-column": (3.35, 2.35),
    "double-column": (7.0, 4.2),
    "two-panel": (7.0, 2.8),
    "four-panel": (7.0, 5.2),
}

def apply_publication_style(preset: str = "single-column") -> tuple[float, float]:
    if preset not in PRESETS:
        raise ValueError(f"Unknown preset: {preset}. Choose from {list(PRESETS)}")
    plt.rcParams.update({
        "font.size": 8.5,
        "axes.labelsize": 8.5,
        "axes.titlesize": 9.5,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.2,
        "lines.markersize": 4.5,
        "figure.dpi": 150,
        "savefig.dpi": 600,
        "savefig.bbox": "tight",
    })
    return PRESETS[preset]

def export_figure(fig, stem: str, out_dir: str = "outputs") -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "svg", "png"):
        fig.savefig(out / f"{stem}.{ext}", dpi=600 if ext == "png" else None, bbox_inches="tight")
