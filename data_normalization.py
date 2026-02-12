import csv

data = [12, 45, 30, 5, 80, 60]

minimum = min(data)
maximum = max(data)

normalized_data = [(value - minimum) / (maximum - minimum) for value in data]

with open("normalized_output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Original_Value", "Normalized_Value"])
    
    for original, norm in zip(data, normalized_data):
        writer.writerow([original, norm])

print("CSV file 'normalized_output.csv' created successfully!")
