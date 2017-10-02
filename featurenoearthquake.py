import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal.trigger import z_detect
from obspy.signal.trigger import plot_trigger
from obspy.signal.trigger import ar_pick
from obspy import UTCDateTime
from obspy.signal.invsim import simulate_seismometer, corn_freq_2_paz
import glob, os
import datetime

import obspy
from obspy.clients.arclink import Client
from obspy.signal.trigger import recursive_sta_lta, trigger_onset
count=1
channeldict = {'BHZ': 1, 'BHN': 2, 'BHE': 3}
import csv
with open('/Users/Nishita/Documents/Research/testing/trainnoearth.csv', 'a') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(["station", "channel","starttime","endtime","label","timeseries1","timeseries2","timeseries3","timeseries4","timeseries5","timeseries6","timeseries7","timeseries8"])

os.chdir("/Volumes/Seagate Expansion Drive/before")
for file in glob.glob("*XX.*JJS*"):
    BHZfile = "/Volumes/Seagate Expansion Drive/before/" + file[0:-4]
    print(BHZfile)

    min1=0
    max1=60
    import csv
    with open('/Users/Nishita/Documents/Research/testing/trainnoearth.csv', 'a') as csvfile:

                #BHZchannel = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) + '*BHZ.SAC', starttime=dt1+p_pick, endtime=dt1+s_pick)

        for i in range(1,30):
            tr_bhz = read(file)
            tr_bhz1 = read(file,starttime=tr_bhz[0].stats.starttime+min1,endtime=tr_bhz[0].stats.starttime+max1)

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
            spamwriter.writerow([tr_bhz1[0].stats.station, tr_bhz1[0].stats.channel,tr_bhz1[0].stats.starttime.timestamp,tr_bhz1[0].stats.endtime.timestamp,0,BHZdata,BHZdata2,BHZdata3,BHZdata4,BHZdata5,BHZdata6,BHZdata7,BHZdata8])
            count=count+1;
            print("count: "+str(count))
            min1=min1+60
            max1=max1+60

            del tr_bhz
