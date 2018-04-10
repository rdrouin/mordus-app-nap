import csv

def group_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id_group":row[0],"fc_code": row[1], "group_name": row[2],"group_type": row[3] ,"group_class": row[4] })
    return table
