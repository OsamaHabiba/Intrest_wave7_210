import glob, os, math, pandas, csv, numpy

from operator import itemgetter

os.chdir("/home/osmium76/intrsw7210/task2/emulsion-data-for-track-multiplicity")

slops= [["XZ","YZ"]]


for file in glob.glob("*_Tracks.csv"):
    tracks = pandas.read_csv(file, usecols=[0,4,5])
    lines = tracks[tracks["trType"]==1]
    for i in range(len(lines)):
        slops.append([math.atan(lines.iat[i,1]),math.atan(lines.iat[i,2])])

os.chdir("/home/osmium76/intrsw7210/task2")



with open('slops.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(slops)


