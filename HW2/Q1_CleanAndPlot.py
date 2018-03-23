import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import numpy.ma as ma
from collections import Counter


def clean_duration(durationData):
    duration_Clean = []
    for value in durationData:
        value = str(value)
        value = value.replace("<","")
        value = value.replace(">", "")
        value = value.replace("~", "")
        value = value.replace("-", " ")
        value = value.replace(".", "")
        time = []
        for v in value.split():
            if v.isdigit():
                time.append(v)
        time = max(time) if time else 0
        if any(sec in value for sec in seconds):
            duration_Clean.append(int(time))
        elif any(min in value for min in minutes):
            duration_Clean.append(int(int(time) * 60))
        elif any(hr in value for hr in hours):
            duration_Clean.append(int(int(time) * 60 * 60))

    duration_Clean = np.array(duration_Clean)
    duration_Clean = duration_Clean[~(np.equal(duration_Clean,0))]
    return duration_Clean


def printMeanMedianMode(data):
    print np.mean(data)
    print np.median(data)
    print ((stats.mode(data))[0])[0]


##
##
##      HW2 Question 1 Part 1
## A boxplot of the duration of UFO sightings of each shape (one boxplot per shape).
##
##
np.set_printoptions(threshold=np.inf)
circleData = pd.read_csv('./Circle.csv')
fireballData = pd.read_csv('./Fireball.csv')
rectangleData = pd.read_csv('./Triangle.csv')

## Time conversion
seconds = ["sec","seconds","secs","second"]
minutes = ["min","minutes", "minute","mins"]
hours = ["hours", "hours","hr"]

## Circle time duration
durationCircleData = circleData['Duration']
durationCircle = clean_duration(durationCircleData)

## Fireball time duration
durationFireballData = fireballData['Duration']
durationFireball = clean_duration(durationFireballData)

## Rectangle time duration
durationRectangleData = rectangleData['Duration']
durationRectangle = clean_duration(durationRectangleData)


## Plot Circle duration
plt.boxplot(durationCircle)
plt.ylabel("Duration of Circle shape UFO sighting ")
plt.ylim([-300,5000])
plt.show()
## Print mean median mode for Circle=
printMeanMedianMode(durationCircle)


## Plot Fireball duration
plt.boxplot(durationFireball)
plt.ylabel("Duration of Fireball shape UFO sighting ")
plt.ylim([-300,3000])
plt.show()
## Print mean median mode for Fireball
printMeanMedianMode(durationFireball)


## Plot Rectangle duration
plt.boxplot(durationRectangle)
plt.ylabel("Duration of Rectangle shape UFO sighting ")
plt.ylim([-300,2500])
plt.show()
## Print mean median mode for Rectangle
printMeanMedianMode(durationRectangle)
