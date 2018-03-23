import pandas as pd
import numpy as np
import numpy
import sys
from collections import Counter

numpy.set_printoptions(threshold=sys.maxint)
## Columns for dataframe
column = ['Location', 'Time', 'Truth']
df_ = pd.DataFrame(columns=column)


## States to its Region
northWest = ['NY','PA' ,'MA' ,'PA' ,'NJ' ,'RI' ,'CT' ,'VT' ,'NH' ,'ME']
midWest = ['ND','SD','NE','KS','MO' ,'IA' ,'MN' ,'WI' ,'IL' ,'IN', 'MI','OH']
west = ['WA','OR' ,'ID' ,'MT' ,'WY' ,'CO' ,'UT' ,'NV' ,'CA' ,'AZ', 'NM', 'HI', 'AK']
south = ['TX','OK' ,'LA' ,'AR' ,'MS' ,'AL' ,'TN' ,'KY' ,'WV' ,'MD', 'DC', 'DE', 'VA', 'NC', 'SC', 'GA', 'FL']


def combineData(data1, truth):
    combinedValue = []
    for row in data1.iterrows():
        location = ''
        time = ''
        ##
        ## Convert State names to region names
        ##
        if any(row[1]['State'] in northWest for data in northWest):
            location = 'NORTHWEST'
        elif any(row[1]['State'] in midWest for data in midWest):
            location = 'MIDWEST'
        elif any(row[1]['State'] in west for data in west):
            location = 'WEST'
        elif any(row[1]['State'] in south for data in south):
            location = 'SOUTH'
        ##
        ## Convert time to Four parts of the Day
        ##
        if len(row[1]['Date / Time'].split(" ")) == 2:
            numTime = int(row[1]['Date / Time'].split(" ")[1].split(":")[0])
            if 0<=numTime and numTime<6:
                time = 'NIGHT'
            if 6 <= numTime and numTime < 12:
                time = 'MORNING'
            if 12 <= numTime and numTime < 18:
                time = 'AFTERNOON'
            if 18 <= numTime and numTime < 24:
                time = 'EVENING'
        if len(location) > 3 and len(time) > 3:
            combinedValue.append([location, time, truth])
    df = pd.DataFrame(combinedValue, columns=['Location', 'Time', 'Truth'])
    return df



def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


def count(data, conditionLoc, conditionTime):
    count = 0
    for row in data.iterrows():
        if row[1][0] == conditionLoc and row[1][1] == conditionTime:
            count += 1
    return count


##  Find Occurence
def countOccurence(data, conditionLoc, conditionTime, conditionTruth):
    count = 0
    for row in data.iterrows():
        if conditionLoc != "" and conditionTime != "":
            if row[1][0] == conditionLoc and row[1][1] == conditionTime and row[1][2] == conditionTruth:
                count += 1
        elif conditionLoc != "":
            if row[1][0] == conditionLoc and row[1][2] == conditionTruth:
                count += 1
        elif conditionTime != "":
            if row[1][1] == conditionTime and row[1][2] == conditionTruth:
                count += 1
    return count


np.set_printoptions(threshold=np.inf)
circleData = pd.read_csv('./CircleTest.csv')
fireballData = pd.read_csv('./FireballTest.csv')
rectangleData = pd.read_csv('./TriangleTest.csv')

## LOC data for each shape
timeStatecircleData = pd.DataFrame(circleData, columns=['State','Date / Time'])
timeStatefireballData = pd.DataFrame(fireballData, columns=['State','Date / Time'])
timeStaterectangleData = pd.DataFrame(rectangleData, columns=['State','Date / Time'])

## Drop all NAN
timeStatecircleData = timeStatecircleData.dropna()
timeStatefireballData = timeStatefireballData.dropna()
timeStaterectangleData = timeStaterectangleData.dropna()

## Replace state name with region
## CIRCLE
df = combineData(timeStatecircleData,"CIRCLE")
print "Circle ",len(df)
df_ = pd.concat([df, df_])
## RECTANGLE
df = combineData(timeStaterectangleData,"RECTANGLE")
print "Rectangle ",len(df)
df_ = pd.concat([df, df_])
## FIREBALL
df = combineData(timeStatefireballData,"FIREBALL")
print "Fireball ",len(df)
df_ = pd.concat([df, df_])
print len(df_) # 5750
# print_full(df_)

count = 0
for row in df_.iterrows():
    # print row[1][0], row[1][1], row[1][2]
    if row[1][0] == "NORTHWEST" and row[1][1] == "EVENING":
        if row[1][2] == "FIREBALL":
            count+=1
    elif row[1][0] == "NORTHWEST" and row[1][1] == "AFTERNOON":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "NORTHWEST" and row[1][1] == "NIGHT":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "NORTHWEST" and row[1][1] == "MORNING":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "MIDWEST" and row[1][1] == "EVENING":
        if row[1][2] == "FIREBALL":
            count+=1
    elif row[1][0] == "MIDWEST" and row[1][1] == "AFTERNOON":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "MIDWEST" and row[1][1] == "NIGHT":
        if row[1][2] == "RECTANGLE":
            count+=1
    elif row[1][0] == "MIDWEST" and row[1][1] == "MORNING":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "WEST" and row[1][1] == "EVENING":
        if row[1][2] == "FIREBALL":
            count+=1
    elif row[1][0] == "WEST" and row[1][1] == "AFTERNOON":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "WEST" and row[1][1] == "NIGHT":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "WEST" and row[1][1] == "MORNING":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "SOUTH" and row[1][1] == "EVENING":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "SOUTH" and row[1][1] == "AFTERNOON":
        if row[1][2] == "CIRCLE":
            count+=1
    elif row[1][0] == "SOUTH" and row[1][1] == "NIGHT":
        if row[1][2] == "RECTANGLE":
            count+=1
    elif row[1][0] == "SOUTH" and row[1][1] == "MORNING":
        if row[1][2] == "CIRCLE":
            count+=1

print "true Positive", str(count)
print "Accuracy ", float(2251.0/5750.0)

# print len(timeStatecircleData)+len(timeStatefireballData)+len(timeStaterectangleData)

# Total = 18337.0
# count_Circle = 4533.0
# count_Rectangle = 4154.0
# count_Fireball = 3900.0

## GINI of the system P(Circle)*P(Regtangle)*P(Rectangle)
# gini_system = ((count_Circle/Total) * (count_Fireball/Total) * (count_Fireball/Total))
# print gini_system ## 0.0368080416351 (0.96319195836)
# print Counter(df_['Location'].tolist())
# print Counter(df_['Time'].tolist())

## Count of Locations
## Counter({'SOUTH': 3784, 'WEST': 3713, 'MIDWEST': 2871, 'NORTHWEST': 2219})

## Count of Time
## Counter({'EVENING': 8539, 'NIGHT': 2069, 'AFTERNOON': 1015, 'MORNING': 964})

count_NorthWest = 2219.0
count_Midwest = 2871.0
count_West = 3713.0
count_South = 3784.0

count_Evening = 8539
count_Night = 2069
count_Afternoon = 1015
count_Morning = 964

##  Gini Index for REGION : 0.14537964431 (0.85462035568)
# print (float(countOccurence(df_,"NORTHWEST","","CIRCLE")*countOccurence(df_,"NORTHWEST","","RECTANGLE")*countOccurence(df_,"NORTHWEST","","FIREBALL"))/(count_NorthWest*count_NorthWest*count_NorthWest)) + \
#       (float(countOccurence(df_,"MIDWEST","","CIRCLE")*countOccurence(df_,"MIDWEST","","RECTANGLE")*countOccurence(df_,"MIDWEST","","FIREBALL"))/(count_Midwest*count_Midwest*count_Midwest)) + \
#       (float(countOccurence(df_,"WEST","","CIRCLE")*countOccurence(df_,"WEST","","RECTANGLE")*countOccurence(df_,"WEST","","FIREBALL"))/(count_West*count_West*count_West)) + \
#       (float(countOccurence(df_,"SOUTH","","CIRCLE")*countOccurence(df_,"SOUTH","","RECTANGLE")*countOccurence(df_,"SOUTH","","FIREBALL"))/(count_South*count_South*count_South))

## GINI Index for Tim : 0.135450586081 (0.86454941391)
# print (float(countOccurence(df_,"","EVENING","CIRCLE")*countOccurence(df_,"","EVENING","RECTANGLE")*countOccurence(df_,"","EVENING","FIREBALL"))/(count_Evening*count_Evening*count_Evening)) + \
#       (float(countOccurence(df_,"","NIGHT","CIRCLE")*countOccurence(df_,"","NIGHT","RECTANGLE")*countOccurence(df_,"","NIGHT","FIREBALL"))/(count_Night*count_Night*count_Night)) + \
#       (float(countOccurence(df_,"","AFTERNOON","CIRCLE")*countOccurence(df_,"","AFTERNOON","RECTANGLE")*countOccurence(df_,"","AFTERNOON","FIREBALL"))/(count_Afternoon*count_Afternoon*count_Afternoon)) + \
#       (float(countOccurence(df_,"","MORNING","CIRCLE")*countOccurence(df_,"","MORNING","RECTANGLE")*countOccurence(df_,"","MORNING","FIREBALL"))/(count_Morning*count_Morning*count_Morning))
#


## GINI GAIN
print 'Region', float(0.96319195836 - 0.85462035568) ## 0.10857160268
print 'Time', float(0.96319195836 - 0.86454941391) ## 0.09864254445

## REGION has high gain using regin as first split
print float(countOccurence(df_,"NORTHWEST","EVENING","CIRCLE"))/float(count(df_,"NORTHWEST","EVENING"))
print float(countOccurence(df_,"NORTHWEST","EVENING","RECTANGLE"))/float(count(df_,"NORTHWEST","EVENING"))
print float(countOccurence(df_,"NORTHWEST","EVENING","FIREBALL"))/float(count(df_,"NORTHWEST","EVENING"))


print float(countOccurence(df_,"NORTHWEST","NIGHT","CIRCLE"))/float(count(df_,"NORTHWEST","NIGHT"))
print float(countOccurence(df_,"NORTHWEST","NIGHT","RECTANGLE"))/float(count(df_,"NORTHWEST","NIGHT"))
print float(countOccurence(df_,"NORTHWEST","NIGHT","FIREBALL"))/float(count(df_,"NORTHWEST","NIGHT"))
print ""

print float(countOccurence(df_,"NORTHWEST","AFTERNOON","CIRCLE"))/float(count(df_,"NORTHWEST","AFTERNOON"))
print float(countOccurence(df_,"NORTHWEST","AFTERNOON","RECTANGLE"))/float(count(df_,"NORTHWEST","AFTERNOON"))
print float(countOccurence(df_,"NORTHWEST","AFTERNOON","FIREBALL"))/float(count(df_,"NORTHWEST","AFTERNOON"))
print ""

print float(countOccurence(df_,"NORTHWEST","MORNING","CIRCLE"))/float(count(df_,"NORTHWEST","MORNING"))
print float(countOccurence(df_,"NORTHWEST","MORNING","RECTANGLE"))/float(count(df_,"NORTHWEST","MORNING"))
print float(countOccurence(df_,"NORTHWEST","MORNING","FIREBALL"))/float(count(df_,"NORTHWEST","MORNING"))
print ""



print float(countOccurence(df_,"MIDWEST","EVENING","CIRCLE"))/float(count(df_,"MIDWEST","EVENING"))
print float(countOccurence(df_,"MIDWEST","EVENING","RECTANGLE"))/float(count(df_,"MIDWEST","EVENING"))
print float(countOccurence(df_,"MIDWEST","EVENING","FIREBALL"))/float(count(df_,"MIDWEST","EVENING"))
print ""

print float(countOccurence(df_,"MIDWEST","NIGHT","CIRCLE"))/float(count(df_,"MIDWEST","NIGHT"))
print float(countOccurence(df_,"MIDWEST","NIGHT","RECTANGLE"))/float(count(df_,"MIDWEST","NIGHT"))
print float(countOccurence(df_,"MIDWEST","NIGHT","FIREBALL"))/float(count(df_,"MIDWEST","NIGHT"))
print ""

print float(countOccurence(df_,"MIDWEST","AFTERNOON","CIRCLE"))/float(count(df_,"MIDWEST","AFTERNOON"))
print float(countOccurence(df_,"MIDWEST","AFTERNOON","RECTANGLE"))/float(count(df_,"MIDWEST","AFTERNOON"))
print float(countOccurence(df_,"MIDWEST","AFTERNOON","FIREBALL"))/float(count(df_,"MIDWEST","AFTERNOON"))
print ""

print float(countOccurence(df_,"MIDWEST","MORNING","CIRCLE"))/float(count(df_,"MIDWEST","MORNING"))
print float(countOccurence(df_,"MIDWEST","MORNING","RECTANGLE"))/float(count(df_,"MIDWEST","MORNING"))
print float(countOccurence(df_,"MIDWEST","MORNING","FIREBALL"))/float(count(df_,"MIDWEST","MORNING"))
print ""



print float(countOccurence(df_,"WEST","EVENING","CIRCLE"))/float(count(df_,"WEST","EVENING"))
print float(countOccurence(df_,"WEST","EVENING","RECTANGLE"))/float(count(df_,"WEST","EVENING"))
print float(countOccurence(df_,"WEST","EVENING","FIREBALL"))/float(count(df_,"WEST","EVENING"))
print ""

print float(countOccurence(df_,"WEST","NIGHT","CIRCLE"))/float(count(df_,"WEST","NIGHT"))
print float(countOccurence(df_,"WEST","NIGHT","RECTANGLE"))/float(count(df_,"WEST","NIGHT"))
print float(countOccurence(df_,"WEST","NIGHT","FIREBALL"))/float(count(df_,"WEST","NIGHT"))
print ""

print float(countOccurence(df_,"WEST","AFTERNOON","CIRCLE"))/float(count(df_,"WEST","AFTERNOON"))
print float(countOccurence(df_,"WEST","AFTERNOON","RECTANGLE"))/float(count(df_,"WEST","AFTERNOON"))
print float(countOccurence(df_,"WEST","AFTERNOON","FIREBALL"))/float(count(df_,"WEST","AFTERNOON"))
print ""

print float(countOccurence(df_,"WEST","MORNING","CIRCLE"))/float(count(df_,"WEST","MORNING"))
print float(countOccurence(df_,"WEST","MORNING","RECTANGLE"))/float(count(df_,"WEST","MORNING"))
print float(countOccurence(df_,"WEST","MORNING","FIREBALL"))/float(count(df_,"WEST","MORNING"))
print ""



## RULES
# "NORTHWEST","EVENING","FIREBALL"
# "NORTHWEST","AFTERNOON","CIRCLE"
# "NORTHWEST","NIGHT","CIRCLE"
# "NORTHWEST","MORNING","CIRCLE"
# "MIDWEST","EVENING","FIREBALL"
# "MIDWEST","NIGHT","RECTANGLE"
# "MIDWEST","AFTERNOON","CIRCLE"
# "MIDWEST","MORNING","CIRCLE"
# "WEST","EVENING","FIREBALL"
# "WEST","NIGHT","CIRCLE"
# "WEST","AFTERNOON","CIRCLE"
# "WEST","MORNING","CIRCLE"
# "SOUTH","EVENING","CIRCLE"
# "SOUTH","NIGHT","RECTANGLE"
# "SOUTH","AFTERNOON","CIRCLE"
# "SOUTH","MORNING","CIRCLE"



print float(countOccurence(df_,"SOUTH","EVENING","CIRCLE"))/float(count(df_,"SOUTH","EVENING"))
print float(countOccurence(df_,"SOUTH","EVENING","RECTANGLE"))/float(count(df_,"SOUTH","EVENING"))
print float(countOccurence(df_,"SOUTH","EVENING","FIREBALL"))/float(count(df_,"SOUTH","EVENING"))
print ""

print float(countOccurence(df_,"SOUTH","NIGHT","CIRCLE"))/float(count(df_,"SOUTH","NIGHT"))
print float(countOccurence(df_,"SOUTH","NIGHT","RECTANGLE"))/float(count(df_,"SOUTH","NIGHT"))
print float(countOccurence(df_,"SOUTH","NIGHT","FIREBALL"))/float(count(df_,"SOUTH","NIGHT"))
print ""

print float(countOccurence(df_,"SOUTH","AFTERNOON","CIRCLE"))/float(count(df_,"SOUTH","AFTERNOON"))
print float(countOccurence(df_,"SOUTH","AFTERNOON","RECTANGLE"))/float(count(df_,"SOUTH","AFTERNOON"))
print float(countOccurence(df_,"SOUTH","AFTERNOON","FIREBALL"))/float(count(df_,"SOUTH","AFTERNOON"))
print ""

print float(countOccurence(df_,"SOUTH","MORNING","CIRCLE"))/float(count(df_,"SOUTH","MORNING"))
print float(countOccurence(df_,"SOUTH","MORNING","RECTANGLE"))/float(count(df_,"SOUTH","MORNING"))
print float(countOccurence(df_,"SOUTH","MORNING","FIREBALL"))/float(count(df_,"SOUTH","MORNING"))
print ""
