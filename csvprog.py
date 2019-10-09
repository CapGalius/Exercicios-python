import csv

path = "/home/galileu/Exercicios-python/Google Stock Market Data - google_stock_data.csv.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader) # Fist line is the reader
data = [row for row in reader] # Read reamining data
print(header)
print(data[0])


#file = open(path)
#for line in file:
#    print(line)
#lines = [line for line in open(path)]
#dataset = [line.strip().split(',') for line in open(path)]
#print(dataset[0])
