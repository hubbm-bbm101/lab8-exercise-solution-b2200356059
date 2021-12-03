import sys
List=[]
with open(sys.argv[1], "r") as f:
    for line in f:
        List.append(line.strip("\n").split(":"))

Students=[]
for i in range(len(List)):
    Students.append(List[i][0])

Universities=[]
for k in range(len(List)):
    Universities.append(List[k][1])


Dict={keys:values for (keys,values) in zip(Students,Universities)}

Names = sys.argv[2]
x= Names.split(",")

for i in x:
    try:
        print("Name:","{},".format(i), "University:",Dict[i])
    except KeyError:
        print("No record of '%s' was found" % i)