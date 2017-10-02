
import matplotlib.pyplot as plt
import numpy as np
import datetime
from obspy.core import read
from obspy.signal.trigger import ar_pick
from obspy.taup import TauPyModel

for i in range(1, 31):
    tr1 = read('/Users/Nishita/Documents/Research/example30/*'+str(i)+'*BHZ.SAC')[0]
    tr2 = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) +'*BHN.SAC')[0]
    tr3 = read('/Users/Nishita/Documents/Research/example30/*'+ str(i) +'*BHE.SAC')[0]



    df = tr1.stats.sampling_rate
    p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df,1.0, 20.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2)
    data = read('/Users/Nishita/Documents/Research/example30/*'+str(i)+'*BHZ.SAC')
    ti=data[0].stats.starttime   #The result is UTC Date Time(2008, 7, 30, 16, 0, 1, 320000)
    #Transfer UTC time to Unix timestamp (second)
    ti_unix=float(ti.strftime("%s.%f"))	#The result is 1217404801.32
    # for example, if you find the aftershock at the 67321th data point, then the standard format should be :
    p_pick_time=float(datetime.datetime.fromtimestamp(ti_unix+ 8*3600+p_pick).strftime('%Y%m%d%H%M%S.%f'))
    s_pick_time=float(datetime.datetime.fromtimestamp(ti_unix+ 8*3600+s_pick).strftime('%Y%m%d%H%M%S.%f'))
    p_time=round(p_pick_time,2)
    s_time=round(s_pick_time,2)
    print("P wave arrival time:")
    print(p_time)
    print("S wave arrival time:")
    print(s_time)
    text_file = open("resultsp.txt", "a")
    text_file.write("\n"+tr1.stats.station+", "+str(p_time)+", "+"P")
    text_file.write("\n"+tr1.stats.station+", "+str(s_time)+", "+"S")
    #text_file.write([tr1.stats.station,round(s_pick_time,2),"S"])
    text_file.close()
    
