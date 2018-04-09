import csv

def csvreader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id_cap_pool":row[0],"cap_pool_name": row[1]})
    return table

# Permet d'appeler la commande avec le pwershell
# mettre des : au boutte de toute.
if __name__ == '__main__':
    result = csvreader("cap_pool.csv")
    print(result[1]["cap_pool_name"])
