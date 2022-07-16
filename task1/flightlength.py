import glob, os, math, pandas, csv

os.chdir("/home/osmium76/intrsw7210/task1/emulsion-data-for-charm-studies")
length_list = [["length"]]

for file in glob.glob("*_Vertices.csv"):

    event = pandas.read_csv(file, usecols=[1,2,3])

    vertix1 = [event.iat[0,0],event.iat[0,1],event.iat[0,2]]
    vertix2 = [event.iat[1,0],event.iat[1,1],event.iat[1,2]]
    
    x = vertix1[0]-vertix2[0]

    y = vertix1[1]-vertix2[1]

    z = vertix1[2]-vertix2[2]

    length = math.sqrt(x**2 + y**2 + z**2)
    length_list.append([length])


os.chdir("/home/osmium76/intrsw7210/task1")

with open('flightlength.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(length_list)

    

        
