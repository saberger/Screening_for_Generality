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

fig, axes = plt.subplots(nrows=7, ncols=8, sharex=True, sharey=True)

i = 1

while i < 57:
        plt.subplot(7, 8, i)
        plt.bar(r, x[i-1], color='lightsteelblue', alpha=0.6, width=width, edgecolor='black', label='Starting Panel')
        plt.bar(r + width, y[i-1], color='cornflowerblue', alpha=0.6, width=width, edgecolor='black', label='1st round addition')
        plt.bar(r + 2 * width, z[i-1], color='royalblue', alpha=0.6, width=width, edgecolor='black', label='2nd round addition')
        plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        i += 1

fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
fig.set_size_inches(32, 18)
plt.xlabel("Panels")
plt.ylabel("Hits/Enzyme")
blue_patch = mpatches.Patch(color='lightsteelblue', label='Starting')
green_patch = mpatches.Patch(color='cornflowerblue', label='1st round addition')
black_patch = mpatches.Patch(color='royalblue', label='2nd round addition')
fig.legend(handles=[blue_patch, green_patch, black_patch], loc='lower center', ncol=5)
plt.show()