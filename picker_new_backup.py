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

def convertformat(tr,slicestarttime):

    #print("starttime: "+str(starttime))
     #The result is UTC Date Time(2008, 7, 30, 16, 0, 1, 320000)
    #ti_unix=float(starttime.strftime("%s.%f"))	#The result is 1217404801.32
    slicestarttime_unix=round(float(slicestarttime.strftime("%s.%f")),2)
    # for example, if you find the aftershock at the 67321th data point, then the standard format should be :
    #offsettime=slicestarttime_unix-ti_unix
    time_submission=round(float(datetime.datetime.fromtimestamp(slicestarttime_unix+ 8*3600+tr).strftime('%Y%m%d%H%M%S.%f')),2)
    # sample format in Beijing time : 20080731001114.53
    print("Validation :"+"slicestarttime: "+ str(slicestarttime)+ " time_submission: "+str(time_submission))

    return time_submission;
count=0
os.chdir("/Users/Nishita/Documents/Research/round2_data/slices/")

for file in glob.glob("*.txt"):
    txtfile = open(file, "r")
    filecontent=txtfile.read()
    onofftime=filecontent.split()
    print(onofftime)
    j=0
    i=0
    #for p in onofftime:
    import csv
    with open('earthquake_mytry2.csv', 'a') as csvfile:
        while i < len(onofftime):


            #print(UTCDateTime(p))
            j=j+1
            BHNfile = "/Users/Nishita/Documents/Research/round2_data/after/" + file[0:-4] + "*BHN*"
            BHEfile = "/Users/Nishita/Documents/Research/round2_data/after/" + file[0:-4] + "*BHE*"
            BHZfile = "/Users/Nishita/Documents/Research/round2_data/after/" + file[0:-4] + "*BHZ*"

            try:
                #tr = read(BHZfile)
                #starttime=tr[0].stats.starttime
                p_pick=0
                s_pick=0
                print(UTCDateTime(onofftime[i]))
                print(UTCDateTime(onofftime[i+1]))
                print("about to start reading")
                tr_bhn = read(BHNfile,starttime=UTCDateTime(onofftime[i]),endtime=UTCDateTime(onofftime[i+1]))
                #print(file[0:-4]+" Starttime:"+onofftime[i]+" endtime:"+onofftime[i+1])

                tr_bhe = read(BHEfile,starttime=UTCDateTime(onofftime[i]),endtime=UTCDateTime(onofftime[i+1]))
                tr_bhz = read(BHZfile,starttime=UTCDateTime(onofftime[i]),endtime=UTCDateTime(onofftime[i+1]))
                #print("finished reading")

                station=tr_bhz[0].stats.station



                df = tr_bhz[0].stats.sampling_rate
                #print("finished reading df")
                p_pick, s_pick = ar_pick(tr_bhz[0].data, tr_bhn[0].data, tr_bhe[0].data, df,1.0, 20.0, 0.2, 0.05, 0.4, 0.1, 3, 8, 0.1, 0.2,True)
                #print("finished reading ar piicker")
                print(file[0:-4]+"p_pick: "+str(p_pick)+" s_pick: "+str(s_pick)+" Of slice: "+str(j))
                tr_bhz.plot()
                del tr_bhz
                del tr_bhn
                del tr_bhe


                p_pick_actual=convertformat(p_pick,UTCDateTime(onofftime[i]))
                s_pick_actual=convertformat(s_pick,UTCDateTime(onofftime[i]))


            except IndexError:
                print("One of the files is missing")
            else:
                if(p_pick>1 and s_pick-p_pick<25 and s_pick>p_pick):

                    count=count+1
                    spamwriter = csv.writer(csvfile, delimiter=',')
                        #l = [(tr1.stats.network,tr1.stats.station, tr1.stats.location, tr1.stats.channel,time_submission,endtime_submission,tr1.stats.sampling_rate,tr1.stats.delta,tr1.stats.npts,tr1.stats.calib,tr1.stats._format,tr1.stats.sac.delta,tr1.stats.sac.b,tr1.stats.sac.e)]
                        #row = zip(*l)

                    spamwriter.writerow([station,p_pick_actual,"P"])
                    spamwriter.writerow([station,s_pick_actual,"S"])
                    print("Count: "+str(count))


            i=i+2

            #tr.plot(type='relative')
            #plt.plot(cft, 'k')
            #plt.show()
            #plot_trigger(tr_n, cftn, 2, 0.5)
