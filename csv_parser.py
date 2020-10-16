from os import listdir
from os.path import isfile, join
import csv
import pandas as pd
import numpy as np
mypath = "./RawData"

rawfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
print(rawfiles)

def parse(fileName):
    rawname = "./RawData/"+fileName
    parsedname = "./ParsedData/"+fileName
    with open(rawname) as f:
        reader = csv.reader(f, delimiter = '|')
        #print(type(reader))
        #print(reader[1,:])
        with open(parsedname, 'w', newline = '') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(reader)

# def parse(fileName):
#     rawname = "./RawData/"+fileName
#     parsedname = "./ParsedData/"+fileName
#     data = np.loadtxt(rawname, delimiter='|')
#     rawfiles = [float(i) for i in listdir(mypath) if isfile(join(mypath,f))]
#     print(data[1,:])

for file in rawfiles:
    print(file)
    parse(file)


