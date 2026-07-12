import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

from pathlib import Path


plt.rcParams["font.family"] = "Arial"

plt.rcParams["mathtext.fontset"] = "stix"

plt.rcParams["pdf.fonttype"] = 42

plt.rcParams["ps.fonttype"] = 42


# Target-level counts from PatSAR-GenTest-200, recomputed using ChatGPT-5

targets = ["ALK", "BTK", "CDK", "c-MET", "EGFR", "GLP-1", "HER2", "IL-17A", "KRAS", "PD-L1"]


counts = pd.DataFrame(

    {

        "Entities": [1425, 1870, 1936, 1436, 1987, 1206, 2020, 1719, 1793, 1434],

        "TP":       [1248, 1574, 1794, 1134, 1711, 1118, 1671, 1454, 1516, 1124],

        "FP":       [31,   12,   8,    11,   18,   24,   8,    17,   15,   6],

        "FN":       [177,  296,  142,  302,  276,  88,   349,  265,  277,  310],

    },

    index=targets

)


# Calculate target-level performance metrics

df = pd.DataFrame(index=targets)

df["Precision"] = counts["TP"] / (counts["TP"] + counts["FP"])

df["Recall"] = counts["TP"] / (counts["TP"] + counts["FN"])

df["F1 score"] = 2 * df["Precision"] * df["Recall"] / (df["Precision"] + df["Recall"])


# PARP core-test counts, recomputed using ChatGPT-5

parp_counts = {

    "Entities": 8226,

    "TP": 6503,

    "FP": 23,

    "FN": 1723,

}


parp_precision = parp_counts["TP"] / (parp_counts["TP"] + parp_counts["FP"])

parp_recall = parp_counts["TP"] / (parp_counts["TP"] + parp_counts["FN"])

parp_f1 = 2 * parp_precision * parp_recall / (parp_precision + parp_recall)


parp_reference = {

    "Precision": parp_precision,

    "Recall": parp_recall,

    "F1 score": parp_f1,

}


# Keep the figure large enough for high-resolution export

fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=150)


positions = np.arange(1, len(df.columns) + 1)


bp = ax.boxplot(

    [df[col].values for col in df.columns],

    positions=positions,

    widths=0.45,

    patch_artist=True,

    showmeans=True,

    meanprops=dict(

        marker="D",

        markersize=5,

        markerfacecolor="white",

        markeredgecolor="black",

        markeredgewidth=1.0

    ),

    medianprops=dict(linewidth=1.8, color="black"),

    boxprops=dict(linewidth=1.4, facecolor="white"),

    whiskerprops=dict(linewidth=1.4, color="black"),

    capprops=dict(linewidth=1.4, color="black"),

    flierprops=dict(

        marker="o",

        markersize=4,

        markerfacecolor="white",

        markeredgecolor="black"

    )

)


# Overlay individual non-PARP target-level data points

rng = np.random.default_rng(1)

for i, col in enumerate(df.columns, start=1):

    jitter = rng.normal(0, 0.035, size=len(df[col]))

    ax.scatter(

        np.full(len(df[col]), i) + jitter,

        df[col].values,

        s=38,

        facecolors="white",

        edgecolors="black",

        linewidths=0.8,

        zorder=3,

        label="Non-PARP targets" if i == 1 else None

    )


# Add PARP core-test performance as filled black circles

ax.scatter(

    positions,

    [parp_reference[col] for col in df.columns],

    s=65,

    facecolors="black",

    edgecolors="black",

    linewidths=0.8,

    zorder=4,

    label="PARP core test set"

)


ax.set_xticks(positions)

ax.set_xticklabels(df.columns, fontsize=13)

ax.set_ylabel("Performance score", fontsize=14)

ax.set_ylim(0.70, 1.02)


ax.tick_params(axis="y", labelsize=12)

ax.yaxis.grid(True, linestyle="--", linewidth=0.7, alpha=0.6)

ax.set_axisbelow(True)


ax.spines["top"].set_visible(False)

ax.spines["right"].set_visible(False)

ax.spines["left"].set_linewidth(1.2)

ax.spines["bottom"].set_linewidth(1.2)


ax.legend(

    frameon=False,

    fontsize=11,

    loc="lower left"

)


plt.tight_layout()


# Save to Desktop

desktop = Path.home() / "Desktop"

desktop.mkdir(exist_ok=True)


base = desktop / "Figure3_performance_distribution_ChatGPT5"


fig.savefig(f"{base}.tiff", dpi=600, bbox_inches="tight", pil_kwargs={"compression": "tiff_lzw"})

fig.savefig(f"{base}.png", dpi=600, bbox_inches="tight")

fig.savefig(f"{base}.pdf", bbox_inches="tight")

fig.savefig(f"{base}.svg", bbox_inches="tight")


print("Saved files to Desktop:")

print(f"{base}.tiff")

print(f"{base}.png")

print(f"{base}.pdf")

print(f"{base}.svg")


print("\\nPARP reference values:")

print(f"Precision: {parp_precision:.4f}")

print(f"Recall: {parp_recall:.4f}")

print(f"F1 score: {parp_f1:.4f}")


plt.show()
