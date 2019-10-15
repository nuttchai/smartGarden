import csv

def writeFile(hum, temp):
    
    data = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in list(csv_reader)[::-1][0:9][::-1]:
            if row == []: break
            data.append(row)
            
    data.append([hum,temp])
    with open('data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
        
#with open('data.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    print(list(csv_reader))