import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

def moving_average(data, window_size):
    """
    Calculates the moving average of a given data array.

    Parameters:
    - data (array-like): The input data array.
    - window_size (int): The size of the moving average window.

    Returns:
    - array-like: The moving average of the input data.
    """
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(data, window, 'same')


# Set the directory path where the xlsx files are located
directory_path = input("Enter the directory path: ")
# Set the output folder path
output_folder = "output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Get a list of all xlsx files in the directory
xlsx_files = glob.glob(os.path.join(directory_path, "*.xlsx"))  # Use os.path.join to handle Windows file paths
xlsx_files = [file_path.lstrip("\\") for file_path in xlsx_files]  # Remove leading backslashes

# Loop over each xlsx file
for file_path in xlsx_files:
    df = pd.read_excel(file_path)

    window_size = 5

    num_columns = len(df.columns)
    x_time = np.arange(0, len(df)*30, 30) # Assuming 30 seconds between every data point
    num_rows = int(np.ceil(num_columns / 12))  # Assuming 12 subplots per row

    fig, axs = plt.subplots(num_rows, 12, figsize=(20, 20))

    slopes = []  # List to store the slopes

    for i, column in enumerate(df.columns):
        data = np.array(df[column].tolist(), dtype=np.float64)  # Convert the column data to a numpy array with float64 data type

        # Fit the moving average only in the first half of the data points
        moving_avg = moving_average(data[:len(data)//2], window_size)

        # Remove the first 5 data points of the moving average
        moving_avg = moving_avg[7:-2]

        row = i // 12
        col = i % 12

        axs[row, col].plot(x_time,data, label='Original Data')
        axs[row, col].plot(x_time[:len(moving_avg)],moving_avg, label='Moving Average Fit')

        # Add linear fit to the moving average
        x_fit = x_time[:len(moving_avg)]
        y_fit = moving_avg[:len(moving_avg)]
        coeffs = np.polyfit(x_fit, y_fit, 1)
        linear_fit = np.polyval(coeffs, x_fit)
        axs[row, col].plot(x_fit, linear_fit, label='Linear Fit')

        slope = coeffs[0]  # Get the slope
        slopes.append(slope)  # Append the slope to the list
    
    # Write the slopes to a file
    # Get the input file name without the extension
    input_file_name = os.path.splitext(file_path)[0]


    # Set the output file path using the input file name
    output_file = os.path.join(output_folder, f"{input_file_name}_slopes.txt")
    with open(output_file, "w") as file:
        for i, slope in enumerate(slopes):
            file.write(str(slope))
            if (i + 1) % 12 == 0:  # Start a new line after every 12 slopes
                file.write("\n")
            else:
                file.write(" ")
    fig.add_subplot(111, frameon=False)
    plt.xlabel("Time (s)")
    plt.ylabel("Absorbance (OD)")
    plt.tight_layout()
    # Save the plot to a PNG file
    plot_file_name = os.path.join(output_folder, f"{input_file_name}_plot.png")
    plt.savefig(plot_file_name)
