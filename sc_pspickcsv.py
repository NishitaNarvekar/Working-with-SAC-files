
import matplotlib.pyplot as plt
import numpy as np
from obspy.core import read
from obspy.signal.trigger import ar_pick
from obspy.taup import TauPyModel

for i in range(1, 31):
    tr1 = read('/Users/Nishita/Documents/Research/example30/*'+str(i)+'*BHZ.SAC')[0]
    tr2 = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) +'*BHN.SAC')[0]
    tr3 = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) +'*BHE.SAC')[0]



    df = tr1.stats.sampling_rate
    p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df,1.0, 20.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2)

    print("P wave arrival time:")
    print(tr1.stats.starttime.timestamp+p_pick)
    print("S wave arrival time:")
    print(tr1.stats.starttime.timestamp+s_pick)
    import csv
    with open('resultsp.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        #l = [(tr1.stats.network,tr1.stats.station, tr1.stats.location, tr1.stats.channel,time_submission,endtime_submission,tr1.stats.sampling_rate,tr1.stats.delta,tr1.stats.npts,tr1.stats.calib,tr1.stats._format,tr1.stats.sac.delta,tr1.stats.sac.b,tr1.stats.sac.e)]
        #row = zip(*l)

        spamwriter.writerow([tr1.stats.network, tr1.stats.station, tr1.stats.channel,tr1.stats.starttime.timestamp,tr1.stats.endtime.timestamp, tr1.stats.sampling_rate, tr1.stats.delta, tr1.stats.npts, p_pick,s_pick])

        #rows = zip(tr1.stats.station,tr1.stats.network)
        #for row in rows:
        	#spamwriter.writerow(row)
