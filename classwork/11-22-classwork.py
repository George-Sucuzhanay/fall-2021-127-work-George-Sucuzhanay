import csv
file = open(movies.csv)
for line in file.readlines():
    l = line.strip().split(',')
    print(len(l))

reader = csv.reader(open("movies.csv"))

for line in reader:
    print(line[6]) # prints only the comedy choices (6th column)
    sum = sum + int(line[6])





