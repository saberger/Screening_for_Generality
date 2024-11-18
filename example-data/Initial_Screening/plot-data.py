import pandas as pd
import matplotlib.pyplot as plt

# Get input file paths
filename = input("Enter path to data file please: ")

# Read data from files
data = pd.read_excel(filename)

# Create dataframes
df = pd.DataFrame(data, columns=['Activity Mean', 'Activity SD', 'div'])

# Clean data
x = df['div'].dropna()
y = df['Activity Mean'].dropna()

# Plot data
plt.scatter(x, y, s=55, c='b', alpha=0.5)
plt.xlabel("Substrate Diversity (Hit count)")
plt.ylabel("Activity Mean [mU /mg$^{IRED}$]")
plt.tight_layout()
plt.show()
