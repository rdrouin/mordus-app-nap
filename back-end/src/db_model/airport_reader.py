import csv

def airport_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"city":row[0],"airportCode": row[1],"level3": row[2],"level2": row[3]})
    return table
