import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Create a dataset
filepath = input("Please enter the filepath for the matrix file: ")
data = pd.read_csv(filepath, delimiter='\t', header=None)

# Default heatmap
akws = {"ha": 'left', "va": 'bottom'}
ax = sns.heatmap(data, cmap="Greens", annot=True, annot_kws=akws, fmt=".3g",
                 cbar_kws={'label': 'Hit count', 'orientation': 'vertical',
                           'pad': 0.01, 'shrink': 0.8}, xticklabels=False,
                 yticklabels=False)
for t in ax.texts:
    trans = t.get_transform()
    offs = matplotlib.transforms.ScaledTranslation(-0.48, 0.48,
                                                   matplotlib.transforms.IdentityTransform())
    t.set_transform(offs + trans)
sns.set_theme(font_scale=0.1)
plt.tight_layout()
plt.show()