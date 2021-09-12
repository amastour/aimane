
import csv
with open('data_history.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    print(spamreader.line_num)
    # for row in spamreader:
    #     print(', '.join(row))