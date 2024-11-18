import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a dataset
filepath = input("Please enter the filepath for the matrix file: ")
f = ['Starting', '1st round addition', '2nd round addition']
x, y, z = np.genfromtxt(filepath, delimiter='', unpack=True)

n = 1
r = np.arange(n)
width = 0.25

fig, axes = plt.subplots(nrows=7, ncols=8, sharex=True, sharey=False)
axes = axes.flatten()

for i in range(57):
    ax = axes[i]  # Get the current subplot
    ax.bar(r, x[i], color='lightsteelblue', alpha=0.6, width=width, edgecolor='black', label='Starting Panel')
    ax.bar(r + width, y[i], color='cornflowerblue', alpha=0.6, width=width, edgecolor='black', label='1st round addition')
    ax.bar(r + 2 * width, z[i], color='royalblue', alpha=0.6, width=width, edgecolor='black', label='2nd round addition')
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ymax = max(x[i], y[i], z[i])
    if ymax > 0:
        ax.set_ylim([0, ymax])
    else:
        ax.set_ylim([0, 5])

# Add a big axis, hide frame
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
fig.set_size_inches(32, 18)
plt.xlabel("Panels")
plt.ylabel("Max Activity [U/mgIRED]")
blue_patch = mpatches.Patch(color='lightsteelblue', label='Starting')
green_patch = mpatches.Patch(color='cornflowerblue', label='1st round addition')
black_patch = mpatches.Patch(color='royalblue', label='2nd round addition')
fig.legend(handles=[blue_patch, green_patch, black_patch], loc='lower center', ncol=5)
plt.show()
