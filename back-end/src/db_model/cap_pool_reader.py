import csv

def cap_pool_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id_cap_pool":row[0],"cap_pool_name": row[1]})
    return table
