from matplotlib import pyplot as plt
import numpy as np


def add_grid(axes):
    """Functions to modify grid"""
    axes.grid(color='grey', linestyle='-', linewidth=0.5, which='major', axis='both')
    axes.grid(color='lightblue', linestyle='-', linewidth=0.5, which='minor', axis='both')
    axes.minorticks_on()


porosity_true = np.array((2, 10, 15, 17, 25, 26, 24, 25, 26, 28, 11, 24))/100
porosity_predicted = np.array((1, 11, 16, 19, 24, 27, 26, 23, 27, 29, 12, 23))/100
porosity_delta = porosity_true-porosity_predicted

fig, axes = plt.subplots(1, 1, figsize=(10, 5), dpi=85,
                         facecolor='white', frameon=True, edgecolor='grey', linewidth=1)

fig.subplots_adjust(wspace=0.2, hspace=0.2, left=0.25, right=0.75, top=0.9, bottom=0.18)

axes.scatter(porosity_true, porosity_predicted)
axes.set_xlabel('Porosity true, v/v', fontsize=10)
axes.set_ylabel('Porosity predicted, v/v', fontsize=10)
axes.set_xlim(0, 0.3)
axes.set_ylim(0, 0.3)
add_grid(axes)
plt.show()