import numpy as np
import matplotlib.pyplot as plt

import obspy


# Read in all files starting with dis.
st = obspy.read("/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160000.D.00.BHN.sac")
print(st)
st += obspy.read("/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160000.D.00.BHZ.sac")
print(st)
st += obspy.read("/Users/Nishita/Documents/Research/sample/after/SC.XJI.2008133160001.D.00.BHE.sac")
print(st)

# sort
st.sort(['starttime'])
# start time in plot equals 0
dt = st[0].stats.starttime.timestamp

# Go through the stream object, determine time range in julian seconds
# and plot the data with a shared x axis
ax = plt.subplot(4, 1, 1)  # dummy for tying axis
for i in range(3):
    plt.subplot(4, 1, i + 1, sharex=ax)
    t = np.linspace(st[i].stats.starttime.timestamp - dt,
                    st[i].stats.endtime.timestamp - dt,
                    st[i].stats.npts)
    plt.plot(t, st[i].data)
print(st)
# Merge the data together and show plot in a similar way
st.merge(method=1)
plt.subplot(4, 1, 4, sharex=ax)
t = np.linspace(st[0].stats.starttime.timestamp - dt,
                st[0].stats.endtime.timestamp - dt,
                st[0].stats.npts)
plt.plot(t, st[0].data, 'r')
plt.show()
