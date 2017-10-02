from obspy.core import read
from obspy.signal.trigger import ar_pick
from obspy.signal.trigger import recursive_sta_lta, trigger_onset
from obspy.signal.trigger import plot_trigger
import glob, os
from obspy import UTCDateTime

os.chdir("/Users/Nishita/Documents/Research/round2_data/after/")
for file in glob.glob("*BHZ*"):

    print(file)

    ex30file = "/Users/Nishita/Documents/Research/round2_data/after/" + file
    singlechannel = read(ex30file)
    starttime = singlechannel[0].stats.starttime
    df = singlechannel[0].stats.sampling_rate

    cft = recursive_sta_lta(singlechannel[0].data, int(2.5* df), int(10*df))
    on_of = trigger_onset(cft, 3.5, 0.5)
    #on_of = on_of[:, 0].tolist()
    print(on_of)
    j=0
    onsettime=[]
    len_n=len(on_of)
    for tup in on_of:
        for item in tup:
            onsettime.append(starttime+item/100)
        j=j+1

    #print(onsettime)


    with open("/Users/Nishita/Documents/Research/round2_data/slices/"+file[0:-4]+".txt", "w") as text_file:
        i = 0
        while i < len(onsettime) - 1:
                start=onsettime[i]

                end=onsettime[i+1]

                if(end-start > 45):
                    start = UTCDateTime(start-5)
                    end = UTCDateTime(start+40)
                    text_file.write("%s" % start)
                    text_file.write("\t")
                    text_file.write("%s" % end)
                    text_file.write("\n")
                    start=start+40
                    end=end

                start = UTCDateTime(start-5)
                end = UTCDateTime(end)

                text_file.write("%s" % start)
                text_file.write("\t")
                text_file.write("%s" % end)
                text_file.write("\n")
                i+=2

    #plot_trigger(singlechannel[0], cft, 1.2, 0.5)


        #singlechannel.plot(outfile=file+'.png')
    #singlechannel.plot()
