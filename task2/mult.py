import glob, os, math, pandas, csv, numpy

from operator import itemgetter

os.chdir("/home/osmium76/intrsw7210/task2/emulsion-data-for-track-multiplicity")

mult= [["mult"]]


for file in glob.glob("*_Tracks.csv"):
    tracks = pandas.read_csv(file)
    
    mult.append([len(tracks)])

os.chdir("/home/osmium76/intrsw7210/task2")



with open('mult.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(mult)


