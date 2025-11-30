import csv

# Headers
headers = ['Name', 'Age', 'City']

# Datas
data = [
    ['Alok', 30, 'New York'],
    ['Bobb', 25, 'Los Angeles'],
    ['Champa', 35, 'Chicago']
]

# Create and write to the CSV file
with open('ex_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header and data row
    writer.writerow(headers)
    writer.writerows(data)

print("CSV file 'my_data.csv' created with headers and data.")