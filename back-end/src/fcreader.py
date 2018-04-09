import csv

def csvreader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"id":row[0],"fc": row[1]})
    return table

# Permet d'appeler la commande avec le pwershell
# mettre des : au boutte de toute.
if __name__ == '__main__':
    result = csvreader("fc.csv")
    print(result[0]["fc"])

if __name__ == '__main__':
    result = csvreader("fc.csv")
    for line in result:
        fc = FlightCompany(line['id'], line['fc'])
        db.session.add(fc)
        db.session.commit()
        
