import csv

resultsName = "Start.txt"

with open("out.txt", "wt") as fout:
    with open("Start.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('"', ''))

#!/usr/bin/env python2
from __future__ import division
 
def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite Simpson's rule, using n subintervals"""
    h = (b - a) / n
    s = f(a) + f(b)
 
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
 
    return s * h / 3
 
print simpson(lambda x:x**9, 0.0, 10.0, 100000)


readcsv = open(resultsName,'rb')
reader = csv.reader(readcsv, delimiter= " ")
unique_test = set()
entries = []
for row in reader:
	entries.append( row)
readcsv.close()

writecsv = open("results.csv",'wb')
writer = csv.writer(writecsv,delimiter=",")
writer.writerows(entries)
writecsv.close()
