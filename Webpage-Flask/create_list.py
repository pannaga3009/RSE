import csv

list = []


# open file
with open('summary.csv', 'r') as f:
    reader = csv.reader(f)

    # read file row by row
    rowNr = 0
    for row in reader:
        # Skip the header row.
        if rowNr >= 1:
            list.append(row)
        # Increase the row number
        rowNr = rowNr + 1

print (list[0])
