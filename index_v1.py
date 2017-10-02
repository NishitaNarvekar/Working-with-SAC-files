from obspy import UTCDateTime
import datetime
import pytz, datetime
from collections import defaultdict

datedict = defaultdict(list)
output = []

f = open('lubo.csv', 'rU' ) #open the file in read universal mode
for line in f:
    cells = line.split(",")
    #output.append(UTCDateTime((cells[0]))) #since we want the first, second and third column

    naive = datetime.datetime.strptime (cells[0], "%Y-%m-%d %H:%M:%S")

    datetime1=UTCDateTime(naive)
    print(UTCDateTime(naive).strftime("%Y-%m-%d"))
    date=(UTCDateTime(cells[0]).strftime("%Y-%m-%d"))

    datedict[(date)].append(datetime1);
    #datedict[int(date)].append(datetime1);

    


f.close()
#date=20141216
#datedict[date].append(datetime1)
print(datedict)
