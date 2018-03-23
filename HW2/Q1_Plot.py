import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from itertools import cycle, islice
import numpy.ma as ma
from collections import Counter


np.set_printoptions(threshold=np.inf)
circleData = pd.read_csv('./Circle.csv')
fireballData = pd.read_csv('./Fireball.csv')
rectangleData = pd.read_csv('./Triangle.csv')


def groupBy(data):
    yearGroupBy = {}
    for time in data:
        year = int("20"+time.split("/")[2].split(" ")[0])
        if year in yearGroupBy:
            yearGroupBy[year] += 1
        else:
            yearGroupBy[year] = 1
    return yearGroupBy

##
##      HW2 Question 1 Part 2
## A time series figure with the number of sightings per year (one line per shape).
##


## Calcualte Yearly Count Data
timeCircleData = circleData['Date / Time']
yearlyCircleData = groupBy(timeCircleData.values)

timeFireballData = fireballData['Date / Time']
yearlyFireballData = groupBy(timeFireballData.values)

timeRectangleData = rectangleData['Date / Time']
yearlyRectangleData = groupBy(timeRectangleData.values)

# print yearlyCircleData
# print yearlyFireballData
# print yearlyRectangleData

# plt.plot(yearlyCircleData.keys(), yearlyCircleData.keys())
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])

plt.plot(range(len(yearlyCircleData)), yearlyCircleData.values())
plt.plot(range(len(yearlyFireballData)), yearlyFireballData.values())
plt.plot(range(len(yearlyRectangleData)), yearlyRectangleData.values())

plt.legend(['Circle','Fireball','Rectangle'],loc='upper left')
plt.show()




stateCircleData = circleData['State']
stateFireballData = fireballData['State']
stateRectangleData = rectangleData['State']
stateCircleData = stateCircleData.dropna()
stateFireballData = stateFireballData.dropna()
stateRectangleData = stateRectangleData.dropna()
state = pd.concat([stateCircleData,stateFireballData,stateRectangleData])
stateFreq = dict((Counter(state)))
print len(stateFreq)
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(stateFreq)))
plt.bar(range(len(stateFreq)), stateFreq.values(), color=my_colors)
plt.xticks(range(len(stateFreq)), stateFreq.keys())
plt.ylabel("Sightings by state")
plt.show()

