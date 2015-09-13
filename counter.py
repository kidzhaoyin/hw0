import csv
import sys

if not len(sys.argv) == 2:
    print 'Usage: python counter.py <inputFileName>'
    exit()

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

print 'total number of records containing Single Malt Scotch: '
print count

f.close()

