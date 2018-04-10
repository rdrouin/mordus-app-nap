import csv

def priorite_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id":row[0],"fc_code": row[1],"group_id": row[2], "rank":row[3] })
    return table
