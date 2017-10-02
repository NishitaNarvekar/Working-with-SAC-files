import matplotlib.pyplot as plt
from obspy.core import read
from obspy.signal.trigger import z_detect
from obspy.signal.trigger import plot_trigger
from obspy.signal.trigger import ar_pick
from obspy import UTCDateTime
from obspy.signal.invsim import simulate_seismometer, corn_freq_2_paz
import glob, os
import datetime


channeldict = {'BHZ': 1, 'BHN': 2, 'BHE': 3}
import csv
with open('/Users/Nishita/Documents/Research/testing/featurenoearthquake.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')

    spamwriter.writerow(["network","station","location", "channel","starttime","endtime","sampling_rate","delta","npts","calib","_format","delta","depmin","depmax","scale","odelta","b","e","o","a","internal0"," t0","t1","t2","t3","t4"," t5","t6","t7","t8","t9","f","resp0","resp1","resp2","resp3","resp4","resp5","resp6","resp7","resp8","resp9","stla","stlo","stel","stdp","evla","evlo","evel","evdp","mag","user0","user1","user2","user3","user4","user5","user6","user7","user8","user9","dist","az","baz","gcarc","internal1","internal2","depmen","cmpaz","cmpinc","xminimum","sac.xmaximum","yminimum","ymaximum","unused6","unused7","unused8","unused9","unused10","unused11","unused12","nzyear","nzjday","nzhour","nzmin","nzsec","nzmsec","nvhdr","norid","nevid","npts","internal3","nwfid","nxsize","nysize","unused13","iftype","idep","iztype","unused14","iinst","istreg","ievreg","ievtyp","iqual","isynth","imagtyp","imagsrc","unused15","unused16","unused17","unused18","unused19"," unused20","unused21","unused22","leven","lpspol","lovrok"," lcalda","unused23","kstnm","sac.kevnm","khole"," ko","ka"," kt0","kt1"," kt2","kt3","sac.kt4","kt5","kt6"," kt7","kt8","kt9","kf"," kuser0","kuser1"," kuser2","kcmpnm","sac.knetwk","kdatrd","kinst","label"])


os.chdir("/Volumes/Seagate Expansion Drive/before")
for file in glob.glob("*XX.*JJS*"):

    st = read(file, debug_headers=True)
    stlen=len(st)
    print(st)

    print(st[0].stats)
    print(st[0].stats.sac.dist)
    print("SAC data is : \n")
    print(st[0].data)

    ti=st[0].stats.starttime   #The result is UTC Date Time(2008, 7, 30, 16, 0, 1, 320000)
	#Transfer UTC time to Unix timestamp (second)
    ti_unix=float(ti.strftime("%s.%f"))	#The result is 1217404801.32
	# for example, if you find the aftershock at the 67321th data point, then the standard format should be :
    time_submission=float(datetime.datetime.fromtimestamp(ti_unix+8*3600+673.21).strftime('%Y%m%d%H%M%S.%f'))

    et=st[0].stats.endtime   #The result is UTC Date Time(2008, 7, 30, 16, 0, 1, 320000)
	#Transfer UTC time to Unix timestamp (second)
    et_unix=float(et.strftime("%s.%f"))	#The result is 1217404801.32
	# for example, if you find the aftershock at the 67321th data point, then the standard format should be :
    endtime_submission=float(datetime.datetime.fromtimestamp(et_unix+8*3600+673.21).strftime('%Y%m%d%H%M%S.%f'))


    import csv
    with open('/Users/Nishita/Documents/Research/testing/featurenoearthquake.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        #l = [("network,"station, st[0].stats.location, st[0].stats.channel,time_submission",endtime_submission,st[0].stats.sampling_rate",st[0].stats.delta,st[0].stats.npts,st[0].stats.calib,st[0].stats._format,st[0].stats.delta","b,st[0].stats. e)]
        #row = zip(*l)
        spamwriter.writerow([1,1, st[0].stats.location, channeldict.get(st[0].stats.channel),time_submission,endtime_submission,st[0].stats.sampling_rate,st[0].stats.delta,st[0].stats.npts,st[0].stats.calib,1,st[0].stats.sac.delta,st[0].stats.sac.depmin,st[0].stats.sac.depmax,st[0].stats.sac.scale,st[0].stats.sac.odelta,st[0].stats.sac.b,st[0].stats.sac.e,st[0].stats.sac.o,st[0].stats.sac.a,st[0].stats.sac.internal0,st[0].stats.sac.t0,st[0].stats.sac.t1,st[0].stats.sac.t2,st[0].stats.sac.t3,st[0].stats.sac.t4,st[0].stats.sac.t5,st[0].stats.sac.t6,st[0].stats.sac.t7,st[0].stats.sac.t8,st[0].stats.sac.t9,st[0].stats.sac.f,st[0].stats.sac.resp0,st[0].stats.sac.resp1,st[0].stats.sac.resp2,st[0].stats.sac.resp3,st[0].stats.sac.resp4,st[0].stats.sac.resp5,st[0].stats.sac.resp6,st[0].stats.sac.resp7,st[0].stats.sac.resp8,st[0].stats.sac.resp9,st[0].stats.sac.stla,st[0].stats.sac.stlo,st[0].stats.sac.stel,st[0].stats.sac.stdp,st[0].stats.sac.evla,st[0].stats.sac.evlo,st[0].stats.sac.evel,st[0].stats.sac.evdp,st[0].stats.sac.mag,st[0].stats.sac.user0,st[0].stats.sac.user1,st[0].stats.sac.user2,st[0].stats.sac.user3,st[0].stats.sac.user4,st[0].stats.sac.user5,st[0].stats.sac.user6,st[0].stats.sac.user7,st[0].stats.sac.user8,st[0].stats.sac.user9,st[0].stats.sac.dist,st[0].stats.sac.az,st[0].stats.sac.baz,st[0].stats.sac.gcarc,st[0].stats.sac.internal1,st[0].stats.sac.internal2,st[0].stats.sac.depmen,st[0].stats.sac.cmpaz,st[0].stats.sac.cmpinc,st[0].stats.sac.xminimum,st[0].stats.sac.xmaximum,st[0].stats.sac.yminimum,st[0].stats.sac.ymaximum,st[0].stats.sac.unused6,st[0].stats.sac.unused7,st[0].stats.sac.unused8,st[0].stats.sac.unused9,st[0].stats.sac.unused10,st[0].stats.sac.unused11,st[0].stats.sac.unused12,st[0].stats.sac.nzyear,st[0].stats.sac.nzjday,st[0].stats.sac.nzhour,st[0].stats.sac.nzmin,st[0].stats.sac.nzsec,st[0].stats.sac.nzmsec,st[0].stats.sac.nvhdr,st[0].stats.sac.norid,st[0].stats.sac.nevid,st[0].stats.sac.npts,st[0].stats.sac.internal3,st[0].stats.sac.nwfid,st[0].stats.sac.nxsize,st[0].stats.sac.nysize,st[0].stats.sac.unused13,st[0].stats.sac.iftype,st[0].stats.sac.idep,st[0].stats.sac.iztype,st[0].stats.sac.unused14,st[0].stats.sac.iinst,st[0].stats.sac.istreg,st[0].stats.sac.ievreg,st[0].stats.sac.ievtyp,st[0].stats.sac.iqual,st[0].stats.sac.isynth,st[0].stats.sac.imagtyp,st[0].stats.sac.imagsrc,st[0].stats.sac.unused15,st[0].stats.sac.unused16,st[0].stats.sac.unused17,st[0].stats.sac.unused18,st[0].stats.sac.unused19,st[0].stats.sac.unused20,st[0].stats.sac.unused21,st[0].stats.sac.unused22,st[0].stats.sac.leven,st[0].stats.sac.lpspol,st[0].stats.sac.lovrok,st[0].stats.sac.lcalda,st[0].stats.sac.unused23,st[0].stats.sac.kstnm,st[0].stats.sac.kevnm,st[0].stats.sac.khole,st[0].stats.sac.ko,st[0].stats.sac.ka,st[0].stats.sac.kt0,st[0].stats.sac.kt1,st[0].stats.sac.kt2,st[0].stats.sac.kt3,st[0].stats.sac.kt4,st[0].stats.sac.kt5,st[0].stats.sac.kt6,st[0].stats.sac.kt7,st[0].stats.sac.kt8,st[0].stats.sac.kt9,st[0].stats.sac.kf,st[0].stats.sac.kuser0,st[0].stats.sac.kuser1,st[0].stats.sac.kuser2,channeldict.get(st[0].stats.sac.kcmpnm),1,st[0].stats.sac.kdatrd,st[0].stats.sac.kinst,0])
