import csv

def priorite_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"fc_code": row[0],"group_id": row[1], "rank":row[2] })
    return table
