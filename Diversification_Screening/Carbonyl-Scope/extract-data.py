import os
import re
import pdfplumber
import csv
import sys

def extract_total_area(pdf_path):
  # Extract text from the PDF file using pdfplumber
  with pdfplumber.open(pdf_path) as pdf:
    pages = pdf.pages
    text = ""
    for page in pages:
      text += page.extract_text(x_tolerance=2, y_tolerance=2)

  # Use regular expressions to find the text between "Signal" matches
  pattern = r"Signal (.*?)(?=Signal)"
  matches = re.findall(pattern, text, re.DOTALL)

  results = []
  for match in matches:
    # Use regular expressions to find the numbers after "Totals"
    totals_pattern = r"Totals.*?([\d.]+(?:e[\+-]?\d+)?)"
    totals_matches = re.findall(totals_pattern, match)
    if totals_matches:
      results.extend(totals_matches)
    else:
      results.extend([0])

  return results

# Get the input directory from command-line arguments
input_dir = sys.argv[1] #Comment when using Windows
#input_dir = input("Enter the directory path: ") #Uncomment when using Windows
# Initialize the output CSV file
# Get the name of the input directory
input_dir_name = os.path.basename(input_dir)

# Generate the output file name based on the input directory name
output_file = f"{input_dir_name}_output.csv"

with open(output_file, "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["Total Area"])

  # Loop over all PDF files in the subfolders
  for root, dirs, files in os.walk(input_dir):
    dirs.sort()  # Sort the directories alphabetically
    for file in files:
      if file.endswith(".pdf"):
        pdf_path = os.path.join(root, file)
        file_dir = os.path.basename(os.path.dirname(pdf_path))
        total_area = extract_total_area(pdf_path)
        writer.writerow([file_dir] + total_area)
  print("Extraction completed. Results written to", output_file)
