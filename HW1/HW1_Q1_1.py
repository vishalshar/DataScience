import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import numpy.ma as ma
from collections import Counter

np.set_printoptions(threshold=np.inf)
data = pd.read_csv('./CAStateBuildingMetrics.csv')
#print len(data.columns)
waterUse = data['Water Use (All Water Sources) (kgal)']
#print waterUse


# Count occerences of department : Counter(departmentName)
departmentNames = data['Department Name']
departmentName = set(departmentNames)
# print len(departmentName)


# Loading and removing annoying NaN's
waterUseWithoutNan = np.asarray(waterUse)
#w_WithoutNan = waterUseWithoutNan[~(np.isnan(waterUseWithoutNan))]
# length difference 1722 - 1643 = 79
# print len(waterUseWithoutNan)

#waterUsageMeanWithoutNan = np.mean(w_WithoutNan)
#print waterUsageMeanWithoutNan # 6913.16334149
# Filling up for the NaN values with Mean of the dataset
#waterUsageMean = (np.sum(w_WithoutNan)+ 79*6913.1633) / 1722
#print waterUsageMean


np.putmask(waterUseWithoutNan, np.isnan(waterUseWithoutNan), 6913.16)
waterUseWithoutNan[waterUseWithoutNan == 0] = 6913.16
# print waterUseWithoutNan


# Mean Median Mode
mean = np.mean(waterUseWithoutNan)
print mean

median = np.median(waterUseWithoutNan)
print median

count = stats.mode(waterUseWithoutNan)
mode = (count[0])[0] # little hack to get the value returned
print mode

plt.boxplot(waterUseWithoutNan)
plt.ylabel("Water Usage")
plt.show()


# Remove outliers anything above 2* mean remove it
q75, q25 = np.percentile(waterUseWithoutNan, [75 ,25])
iqr = q75 - q25

dataWithoutOutlier = waterUseWithoutNan[((-1.5*iqr)<=waterUseWithoutNan)&(waterUseWithoutNan<=(1.5*iqr))]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(dataWithoutOutlier)

# Adding label and setting limit for y-axis
plt.ylabel("Water Usage")
plt.ylim([-600,2000])
plt.show()

print np.mean(dataWithoutOutlier)
print np.median(dataWithoutOutlier)
print ((stats.mode(dataWithoutOutlier))[0])[0]

