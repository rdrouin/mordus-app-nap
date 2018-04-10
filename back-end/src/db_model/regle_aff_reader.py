import csv

def regle_aff_reader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"drag_capacity_from":row[0],"drag_capacity_to": row[1],"drag_type": row[2],"drag_value": row[3],"propagation": row[4],"condition_type": row[5]  ,"condition_value": row[6]})
    return table
