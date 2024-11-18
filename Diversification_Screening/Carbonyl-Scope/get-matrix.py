import pandas as pd

file_path = input("Enter the file path: ")
df = pd.read_excel(file_path)
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = df.sort_values(by='Combination')
hitcount = df['Combination'].value_counts(sort=False)

# Print hitcount and combination in a matrix file
matrix_df = pd.DataFrame({'Combination': hitcount.index, 'Hitcount': hitcount.values})
matrix_df.to_csv('matrix.csv', index=False)
