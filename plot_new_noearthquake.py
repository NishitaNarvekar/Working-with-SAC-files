from obspy.core import read
from obspy.signal.trigger import ar_pick
import glob, os

os.chdir("/Volumes/Seagate Expansion Drive/before")
for file in glob.glob("*.BHZ*"):
    BHZfile = "/Volumes/Seagate Expansion Drive/before/" + file[0:-4]
    print(BHZfile)

    min1=0
    max1=60

    for i in range(1,30):
        tr_bhz = read(BHZfile + "*.BHZ")
        tr_bhz1 = read(BHZfile + "*.BHZ",starttime=tr_bhz[0].stats.starttime+min1,endtime=tr_bhz[0].stats.starttime+max1)
        tr_bhz1.plot(outfile="/Users/Nishita/Documents/Research/bluemix/"+file+'.png')
        min1=min1+60
        max1=max1+60
