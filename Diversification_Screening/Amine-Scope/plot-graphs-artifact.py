import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.legendre as leg
import glob
import os

def fit_legender(x_fit,data_fit):
    V = leg.legvander(x_fit, deg)
    coeffs = np.linalg.lstsq(V, data_fit)[0]
    g = leg.legval(x_fit, coeffs)
    coeffsd = leg.legder(coeffs, m=1) # get derivative
    coeffsdd = leg.legder(coeffs, m=2)# get second derivative
    h = leg.legval(x_fit, coeffsdd)
    r = leg.legroots(h)
    r = np.real(r)
    k = leg.legval(r, coeffsd)
    d = leg.legval(r, coeffs) - k * r
    d = np.max(d)
    k = np.min(np.real(k))
    start = np.mean(data[:7]) #estimate how step the curve is
    end = np.mean(data[-20:]) #based on the first and last points
    if abs(end-start) < 500:# fit a linear if the curve is not steep
        coef = np.polyfit(x_fit, data_fit, 1)
        poly1d_fn = np.poly1d(coef)
        return coef[0], g, coef[1]
    else:
        return k, g, d

# Set the directory path where the xlsx files are located
directory_path = input("Enter the directory path: ")
# Set the output folder path
output_folder = "output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all xlsx files in the directory
xlsx_files = glob.glob(directory_path + "/*.xlsx")
deg = 3

# Loop over each xlsx file
for file_path in xlsx_files:
    df = pd.read_excel(file_path, na_values='overflow')
    num_columns = len(df.columns)
    x_time = np.arange(0, len(df)*30, 30) # Assuming 30 seconds between every data point
    num_rows = int(np.ceil(num_columns / 12))  # Assuming 12 subplots per row
    fig, axs = plt.subplots(num_rows, 12, figsize=(20, 20))

    slopes = []  # List to store the slopes

    for i, column in enumerate(df.columns):
        data = df[column].tolist()
        x_fit = x_time[30:len(data)] #remove first 30 points and fit till end 
        data_fit = data[30:len(data)]
        # Perform the fitting and save the function and slope
        slope, g, d = fit_legender(x_fit,data_fit)
        v = slope * np.array(x_fit) + d # tangent

        row = i // 12
        col = i % 12

        axs[row, col].plot(x_time,data, label='Original Data')
        axs[row, col].plot(x_fit,g, label='Legendre polynominal fit')
        axs[row, col].plot(x_fit,v, label='Tangent')

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
    # Create a single legend for all subplots
    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right')
    plt.tight_layout()
    # Save the plot to a PNG file
    plot_file_name = os.path.join(output_folder, f"{input_file_name}_plot.png")
    plt.savefig(plot_file_name)
