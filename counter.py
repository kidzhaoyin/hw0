import csv
import sys

f = open(sys.argv[1],'r')
reader = csv.reader(f)
count = 0
for row in reader:
    line = ""
    for word in row:
	line += word
	line += " "
    if "single malt scotch" in line.lower():
        count += 1

print count

f.close()

