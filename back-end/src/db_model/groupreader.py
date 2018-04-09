import csv

def csvreader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id_group":row[0],"group_name": row[1],"group_type": row[2] })
    return table

# Permet d'appeler la commande avec le pwershell
# mettre des : au boutte de toute.
if __name__ == '__main__':
    result = csvreader("group.csv")
    print(result[1]["group_name"])
