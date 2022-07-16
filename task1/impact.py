import glob, os, math, pandas, csv, numpy

from operator import itemgetter

os.chdir("/home/osmium76/intrsw7210/task1/emulsion-data-for-charm-studies")

ip = [["ip"]]
prim_ver= []

for file in glob.glob("*_Vertices.csv"):

    event = pandas.read_csv(file, usecols=[1,2,3])

    vertix = [int(file.replace("_Vertices.csv","")),event.iat[0,0],event.iat[0,1],event.iat[0,2]]

    prim_ver.append(vertix)

prim_ver = sorted(prim_ver, key=itemgetter(0))




track_cor= []
for file in glob.glob("*_TrackLines.csv"):

    event = pandas.read_csv(file)
    track = event[event["trType"]==10] 

    for i in range(len(track)):
        track_cor.append([int(file.replace("_TrackLines.csv","")), track.iat[i,1],track.iat[i,2],track.iat[i,3],track.iat[i,4],track.iat[i,5],track.iat[i,6]])

track_cor = sorted(track_cor, key=itemgetter(0))



for ver in prim_ver:

    for track in track_cor:

        if ver[0] == track[0]:
            p1 = numpy.array(track[1:4])
            p2 = numpy.array(track[4:])
            p = numpy.array(ver[1:])
            imp = numpy.abs(numpy.linalg.norm(numpy.cross(p2-p1,p-p1)/numpy.linalg.norm(p2-p1)))
            ip.append([imp])


os.chdir("/home/osmium76/intrsw7210/task1")



with open('impactParameter.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(ip)



