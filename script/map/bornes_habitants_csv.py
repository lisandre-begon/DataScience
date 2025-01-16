import csv

# Path to the CSV file
csv_file_path = '../../data/processed/grouped_borne.csv'


# Open the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    
    # Read and print each row
    for row in csv_reader:
        print(row)