import csv

def csvreader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id":row[0],"fc_code": row[1],"group_id": row[2], "rank":row[3] })
    return table

# Permet d'appeler la commande avec le pwershell
# mettre des : au boutte de toute.
if __name__ == '__main__':
    result = csvreader("priorite.csv")
    print(result[1]["group_id"])
