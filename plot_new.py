from obspy.core import read
from obspy.signal.trigger import ar_pick
import glob, os

os.chdir("/Users/Nishita/Documents/Research/example30/")
for file in glob.glob("*"):

    print(file)

    ex30file = "/Users/Nishita/Documents/Research/example30/*" + file
    singlechannel = read(ex30file)
    print(singlechannel[0].stats)


    #singlechannel.plot(outfile=file+'.png')
    singlechannel.plot()
