# Publication Figure Skill

## Purpose

Transform an existing Matplotlib figure or plotting script into a publication-ready academic graphic while preserving the underlying data, statistical meaning, labels, and scientific interpretation.

## Inputs

Prefer one or more of:
- plotting code
- dataframe plus plotting instructions
- current figure screenshot plus source code
- target journal or conference
- target figure width

If width is not provided, use single-column 3.35 in or double-column 7.0 in.

## Workflow

1. Preserve scientific content. Do not change numerical values, remove observations, hide uncertainty, or reorder groups in a misleading way.
2. Set output geometry first. Design for final manuscript width, not a large screen preview.
3. Improve typography. Use one font family, restrained title sizes, and legible labels after downscaling.
4. Improve layout. Reduce unnecessary padding, prevent clipping, and place legends away from dense data.
5. Improve visual hierarchy. Emphasize data, not decoration. Keep line widths and marker sizes consistent.
6. Improve accessibility. Do not rely on color alone. Use marker or line-style redundancy when useful.
7. Export vector PDF and SVG plus 600 dpi PNG.

## Default Matplotlib settings

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
    })

Do not force a specific font if it is unavailable. Prefer a widely available serif or sans-serif family that matches the manuscript.

## Response format

Return revised plotting code, a short list of changes, export files or export commands, and any remaining risks such as unreadable labels or too many categories.
