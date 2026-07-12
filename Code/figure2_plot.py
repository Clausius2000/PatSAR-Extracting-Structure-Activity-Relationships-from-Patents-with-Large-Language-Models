import numpy as np

import matplotlib.pyplot as plt

from pathlib import Path


plt.rcParams["font.family"] = "Arial"

plt.rcParams["mathtext.fontset"] = "stix"

plt.rcParams["pdf.fonttype"] = 42

plt.rcParams["ps.fonttype"] = 42


# Prompt versions

prompt_versions = np.arange(1, 16)

x_labels = [f"P{i}" for i in prompt_versions]


# Development-stage FNR values (%)

# Rename from training/validation to avoid implying parameter-level model training

prompt_refinement_fnr = [42, 35, 30, 28, 27, 23, 22, 20, 5, 5, 6, 5, 7, 5, 5]

development_monitoring_fnr = [72, 65, 60, 55, 63, 48, 46, 44, 21, 28, 18, 20, 18, 18, 18]


fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=150)


# Plot measured values directly

ax.plot(

    prompt_versions,

    prompt_refinement_fnr,

    marker="o",

    linewidth=2.0,

    markersize=5,

    label="Prompt-refinement subset"

)


ax.plot(

    prompt_versions,

    development_monitoring_fnr,

    marker="s",

    linewidth=2.0,

    markersize=5,

    label="Development-monitoring subset"

)


# Optional annotations for key prompt-strategy changes

ax.axvline(x=9, linestyle="--", linewidth=1.0, alpha=0.7)

ax.text(

    9.15, 68,

    "LtM + zero-shot CoT\\nintroduced",

    fontsize=9,

    va="top"

)


ax.axvline(x=12, linestyle="--", linewidth=1.0, alpha=0.7)

ax.text(

    12.15, 68,

    "Few-shot examples\\nand corrective rules",

    fontsize=9,

    va="top"

)


# Axis labels

ax.set_xlabel("Prompt version", fontsize=12)

ax.set_ylabel("False-negative rate (FNR, %)", fontsize=12)


# Ticks and limits

ax.set_xticks(prompt_versions)

ax.set_xticklabels(x_labels, fontsize=10)

ax.set_ylim(0, 80)

ax.set_xlim(0.7, 15.3)


# Grid and styling

ax.yaxis.grid(True, linestyle="--", linewidth=0.6, alpha=0.6)

ax.set_axisbelow(True)


ax.spines["top"].set_visible(False)

ax.spines["right"].set_visible(False)

ax.spines["left"].set_linewidth(1.2)

ax.spines["bottom"].set_linewidth(1.2)


ax.tick_params(axis="y", labelsize=10)

ax.legend(frameon=False, fontsize=10, loc="upper right")


plt.tight_layout()


# Save to Desktop

desktop = Path.home() / "Desktop"

desktop.mkdir(exist_ok=True)


base = desktop / "Figure2_development_stage_FNR"


fig.savefig(f"{base}.tiff", dpi=600, bbox_inches="tight", pil_kwargs={"compression": "tiff_lzw"})

fig.savefig(f"{base}.png", dpi=600, bbox_inches="tight")

fig.savefig(f"{base}.pdf", bbox_inches="tight")

fig.savefig(f"{base}.svg", bbox_inches="tight")


print("Saved files to Desktop:")

print(f"{base}.tiff")

print(f"{base}.png")

print(f"{base}.pdf")

print(f"{base}.svg")


plt.show()
