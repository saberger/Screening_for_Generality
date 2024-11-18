import pandas as pd
import openpyxl
import glob
import os

# Ask for user input
directory_path = input("Enter the directory path: ")
# Set the output folder path
output_folder = os.path.join(directory_path, "output")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all XLSX files in the directory
xlsx_files = glob.glob(directory_path + "/*.xlsx")

# Loop over each XLSX file
for file_path in xlsx_files:

    # Read the data from the xlsx file
    df = pd.read_excel(file_path)

    # Ignore the first lines till the Match Cycle 1+2 lines and the first column
    raw_row_index = df[df.iloc[:, 0].str.contains('^Cycle 1*', regex=True, na=False)].index[0]
    df = df.iloc[raw_row_index+3:,1:]
    # Split the dataframe into multiple tables
    tables = []
    skip_rows = 4
    for i in range(0, len(df), 8 + skip_rows):
        table = df.iloc[i:i+8, :12]
        tables.append(table)

    # Create a new workbook
    new_workbook = openpyxl.Workbook()
    new_sheet = new_workbook.active

    # Iterate through the tables
    for i, table in enumerate(tables):
        # Reshape the table to a single line
        reshaped_table = table.values.flatten()

        # Write the reshaped table to the new sheet
        row = i + 1
        for j, value in enumerate(reshaped_table):
            column = j + 1
            new_sheet.cell(row=row, column=column, value=value)

    # Save the new workbook
    new_file_name = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + "_new.xlsx")
    new_workbook.save(new_file_name)