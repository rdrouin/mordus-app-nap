
import csv
import datetime
#import pandas
def csvreader(file):
    table = []
    with open(file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        next(spamreader, None)  # skip the headers
        for row in spamreader:
            table.append({"date":row[0],"heure": row[1],"noVol": row[2], "fc":row[2][:2],"aeronef": row[3],"od": row[4],"secteur": row[5]})
    return table

# Permet d'appeler la commande avec le pwershell
# mettre des : au boutte de toute.
if __name__ == '__main__':
    result = csvreader("vols.csv")
    print(result[10]["fc"])
