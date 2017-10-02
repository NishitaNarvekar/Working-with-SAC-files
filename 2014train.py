import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal.trigger import z_detect
from obspy.signal.trigger import plot_trigger
from obspy.signal.trigger import ar_pick
from obspy import UTCDateTime
#from obspy.signal.invsim import simulate_seismometer, corn_freq_2_paz
import glob, os
import datetime


import obspy
from obspy.clients.arclink import Client
from obspy.signal.trigger import recursive_sta_lta, trigger_onset

import pytz, datetime
from collections import defaultdict

datedict = defaultdict(list)
output = []

f = open('lubo_index_earthquake.csv', 'rU' ) #open the file in read universal mode
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

count=1
channeldict = {'BHZ': 1, 'BHN': 2, 'BHE': 3}
import csv
with open('/Users/Nishita/Documents/Research/testing/trainearthquakeJJS_maxAmp_allstation.csv', 'a') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(["station", "channel","starttime","endtime","npts","e","max_amp","std_dev","label","timeseries1","timeseries2","timeseries3","timeseries4","timeseries5","timeseries6","timeseries7","timeseries8"])

os.chdir("/Users/Nishita/2014sacdata/")

for file in glob.glob("*.SAC*"):

    print(file)
    min1=0
    max1=60
    import csv
    with open('/Users/Nishita/Documents/Research/testing/trainearthquakeJJS_maxAmp_allstation.csv', 'a') as csvfile:

        #earthfile = "/Users/Nishita/Documents/Research/round2_data/after/" + file[0:-4] + "*"


                #BHZchannel = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) + '*BHZ.SAC', starttime=dt1+p_pick, endtime=dt1+s_pick)


        tr_bhz = read(file)
        starttime1=tr_bhz[0].stats.starttime
        startdate=(UTCDateTime(starttime1).strftime("%Y-%m-%d"))
        #datedict.get('2014-12-21')
        try:
            if(datedict.get(startdate)):
                start=datedict.get(startdate)
                for s in start:
                    print(s)


                    tr_bhz1 = read(file,starttime=s,endtime=s+60,debug_headers=True)
                    tr = tr_bhz1[0].data
                    print(tr_bhz1[0].stats)
                    tr_max = tr.max()
                    tr_std = tr.std()
                    #tr_bhz1.plot()
                    tr_bhz1.write("/Users/Nishita/Documents/Research/tmp/BHZdata.txt", format="TSPAIR")
                    f = open('/Users/Nishita/Documents/Research/tmp/BHZdata.txt', 'r')  # We need to re-open the file

                    BHZdata = f.read(30000).replace("\n"," ")
                    BHZdata2 = f.read(30000).replace("\n"," ")
                    BHZdata3 = f.read(30000).replace("\n"," ")
                    BHZdata4 = f.read(30000).replace("\n"," ")
                    BHZdata5 = f.read(30000).replace("\n"," ")
                    BHZdata6 = f.read(30000).replace("\n"," ")
                    BHZdata7 = f.read(30000).replace("\n"," ")
                    BHZdata8 = f.read(30000).replace("\n"," ")
                                #print(BHZdata)
                    spamwriter = csv.writer(csvfile, delimiter=',')
                                #l = [(st[0].stats.network,st[0].stats.station, st[0].stats.location, st[0].stats.channel,time_submission,endtime_submission,st[0].stats.sampling_rate,st[0].stats.delta,st[0].stats.npts,st[0].stats.calib,st[0].stats._format,st[0].stats.sac.delta,st[0].stats.sac.b,st[0].stats.sac.e)]
                                #row = zip(*l)
                    spamwriter.writerow([tr_bhz1[0].stats.station, tr_bhz1[0].stats.channel,tr_bhz1[0].stats.starttime.timestamp,tr_bhz1[0].stats.endtime.timestamp,tr_bhz1[0].stats.npts,tr_bhz1[0].stats.sac.e,tr_max,tr_std,1,BHZdata,BHZdata2,BHZdata3,BHZdata4,BHZdata5,BHZdata6,BHZdata7,BHZdata8])
                    count=count+1;
                    print("count: "+str(count))


                    del tr_bhz1

        except IndexError:
            print("One of the files is missing")
