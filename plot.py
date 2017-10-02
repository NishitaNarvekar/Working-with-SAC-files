from obspy.core import read
from obspy.signal.trigger import ar_pick

tr1 = read('/Users/Nishita/Documents/Research/example30/01.JMG.BHZ.SAC')[0]
tr2 = read('/Users/Nishita/Documents/Research/example30/01.JMG.BHN.SAC')[0]
tr3 = read('/Users/Nishita/Documents/Research/example30/01.JMG.BHE.SAC')[0]
df = tr1.stats.sampling_rate

#p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df,0.5, 20.0, 5.0, 0.05, 5.0, 0.5, 3, 5, 0.2, 0.05,True)
p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df,1.0, 20.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2,True)
singlechannel = read("/Users/Nishita/Documents/Research/example30/02.PWU.BHZ.SAC")
dt1 = singlechannel[0].stats.starttime

print("P wave arrival time:")
print(p_pick)
print("S wave arrival time:")
print(s_pick)

singlechannel.plot(type='relative')
