import csv
from datetime import datetime

path = "/home/galileu/Exercicios-python/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader) # Fist line is the reader
data = []
for row in reader:
    # row = [Date, Open, High, Low , Close, Volume, Adj. Close]
    date =  datetime.strptime(row[0], '%m/%d/%Y')
    open_price =  float(row[1]) #open is a builtin func 
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price,high,low,close,volume,adj_close])
print(data[0])


#file = open(path)
#for line in file:
#    print(line)
#lines = [line for line in open(path)]
#dataset = [line.strip().split(',') for line in open(path)]
#print(dataset[0])
