from obspy.core import read
from obspy.signal.trigger import ar_pick
tr1 = read('/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160000.D.00.BHN.sac')[0]
tr2 = read('/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160000.D.00.BHZ.sac')[0]
tr3 = read('/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160001.D.00.BHE.sac')[0]
df = tr1.stats.sampling_rate
p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df,1.0, 20.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2)
print(p_pick)

print(s_pick)
