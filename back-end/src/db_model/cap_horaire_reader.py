import csv

def cap_horaire_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id_cap_horaire":row[0],"cap_value": row[1],"cap_timestamp": row[2], "user_id":row[3] })
    return table
