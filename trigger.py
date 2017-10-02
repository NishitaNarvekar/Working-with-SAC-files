import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal.trigger import z_detect
from obspy.signal.trigger import plot_trigger
from obspy.signal.trigger import ar_pick

import obspy
from obspy.clients.arclink import Client
from obspy.signal.trigger import recursive_sta_lta, trigger_onset
import os



#print(tr_n.stats.channel+"starttime"+str(tr_n.stats.starttime))



for i in range(237, 238):
    tr = read('/Volumes/Seagate Expansion Drive/after/*'+'.2008'+str(i)+'*')

    tr_n = tr.select(component="N")[0]
    dtn=tr_n.stats.starttime
    print("BHN "+str(tr_n.stats.starttime)+" "+str(tr_n.stats.endtime))
    #tr_n.plot(type='relative')

    tr_e = tr.select(component="E")[0]
    dte=tr_e.stats.starttime
    print("BHE "+str(tr_e.stats.starttime)+" "+str(tr_e.stats.endtime))

    tr_z = tr.select(component="Z")[0]
    dtz=tr_z.stats.starttime
    print("BHZ "+str(tr_z.stats.starttime)+" "+str(tr_z.stats.endtime))
    #tr = read('/Users/Nishita/Documents/Research/example30/03.QCH.BHZ.SAC')
    #tr = read('/Users/Nishita/Documents/Research/sample/before/SC.XJI.2008131160000.D.00.BHZ.sac')
    #tr.filter('bandpass', freqmin=10, freqmax=20)  # optional prefiltering
    del tr
    #------------BHN-----------------------------------

    dfn = tr_n.stats.sampling_rate

    # Characteristic function and trigger onsets
    #cft = recursive_sta_lta(tr[0].data, int(2.5 * df), int(10. * df))

    cftn = z_detect(tr_n.data, int(10 * dfn))
    on_of_n = trigger_onset(cftn, 2, 0.5)

    j=0
    onsettime=[]
    print("BHN")
    print(on_of_n)
    len_n=len(on_of_n)
    for tup in on_of_n:
        for item in tup:
            onsettime.append(item)
        j=j+1
        #print("aahhh1 "+str(dtn+onsettime[0]/100)+str(dtn+onsettime[1]/100))
        tr_bhn=read('/Volumes/Seagate Expansion Drive/after/*'+'.2008'+str(i)+'*.BHN*',starttime=(dtn+onsettime[0]/100-10),endtime=(dtn+onsettime[1]/100+10))[0]
        #print("aahhh2"+str(onsettime[0])+str(onsettime[1]))
        tr_bhe=read('/Volumes/Seagate Expansion Drive/after/*'+'.2008'+str(i)+'*.BHE*',starttime=(dte+onsettime[0]/100-10),endtime=(dte+onsettime[1]/100+10))[0]
        #print("aahhh3"+str(onsettime[0])+str(onsettime[1]))
        tr_bhz=read('/Volumes/Seagate Expansion Drive/after/*'+'.2008'+str(i)+'*.BHZ*',starttime=(dtz+onsettime[0]/100-10),endtime=(dtz+onsettime[1]/100+10))[0]
        #print("aahhh4"+str(onsettime[0])+str(onsettime[1]))
        onsettime[:] = []
        df = tr_bhz.stats.sampling_rate
        p_pick, s_pick = ar_pick(tr_bhz.data, tr_bhn.data, tr_bhe.data, df,1.0, 20.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2)
        print("p_pick: "+str(p_pick)+" s_pick: "+str(s_pick)+" Of slice: "+str(j))
        tr_bhz.plot(type='relative')
        del tr_bhn
        del tr_bhe
        del tr_bhz
    #tr.plot(type='relative')
    #plt.plot(cft, 'k')
    #plt.show()
    #plot_trigger(tr_n, cftn, 2, 0.5)

    #------------------BHE------------------------------------

    dfe = tr_e.stats.sampling_rate

    # Characteristic function and trigger onsets
    #cft = recursive_sta_lta(tr[0].data, int(2.5 * df), int(10. * df))

    cfte = z_detect(tr_e.data, int(10 * dfe))
    on_of_e = trigger_onset(cfte, 2, 0.5)
    print("BHE")
    print(on_of_e)
    #tr.plot(type='relative')
    #plt.plot(cft, 'k')
    #plt.show()
    #plot_trigger(tr_e, cfte, 2, 0.5)
