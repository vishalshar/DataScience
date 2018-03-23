import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


np.set_printoptions(threshold=np.inf)
data = pd.read_csv('./CAStateBuildingMetrics.csv')
waterUse_DeptNames = pd.DataFrame(data, columns=['Water Use (All Water Sources) (kgal)','Department Name'])


# Count occerences of department : Counter(departmentName)
# departmentNames = data['Department Name']
# departmentName = set(departmentNames)
# print departmentName
# print Counter(departmentNames)


# Find top 5 departments
# California Department of Transportation : 443
# California Department of Forestry and Fire Protection: 313
# Department of Parks and Recreation: 208
# California Highway Patrol: 107
# California Military Department: 103


# California Department of Transportation
deptWaterUsage = (waterUse_DeptNames.loc[waterUse_DeptNames['Department Name'] == 'California Department of Transportation'])['Water Use (All Water Sources) (kgal)']
transportDept = deptWaterUsage.values

# find mean of array without NaN and replace NaN with mean and replace all zeros with mean
transportDept_W_NaN = transportDept[~(np.isnan(transportDept))]
np.putmask(transportDept, np.isnan(transportDept), np.mean(transportDept_W_NaN))
transportDept[transportDept == 0] = np.mean(transportDept_W_NaN)

print np.mean(transportDept)
print np.median(transportDept)
print ((stats.mode(transportDept))[0])[0]

plt.boxplot(transportDept)
plt.ylabel("Transport Department Water Usage")
plt.ylim([-300,10000])
plt.show()


# California Department of Forestry and Fire Protection
forestryWaterUsage = (waterUse_DeptNames.loc[waterUse_DeptNames['Department Name'] == 'California Department of Forestry and Fire Protection'])['Water Use (All Water Sources) (kgal)']
forestryDept = forestryWaterUsage.values

# find mean of array without NaN and replace NaN with mean and replace all zeros with mean
forestryDept_W_NaN = forestryDept[~(np.isnan(forestryDept))]
np.putmask(forestryDept, np.isnan(forestryDept), np.mean(forestryDept_W_NaN))
forestryDept[forestryDept == 0] = np.mean(forestryDept_W_NaN)

print np.mean(forestryDept)
print np.median(forestryDept)
print ((stats.mode(forestryDept))[0])[0]

plt.boxplot(forestryDept)
plt.ylabel("Forestry and Fire Protection Department Water Usage")
plt.ylim([-300,8000])
plt.show()


# Department of Parks and Recreation
parksWaterUsage = (waterUse_DeptNames.loc[waterUse_DeptNames['Department Name'] == 'Department of Parks and Recreation'])['Water Use (All Water Sources) (kgal)']
parksDept = parksWaterUsage.values

# find mean of array without NaN and replace NaN with mean and replace all zeros with mean
parksDept_W_NaN = parksDept[~(np.isnan(parksDept))]
np.putmask(parksDept, np.isnan(parksDept), np.mean(parksDept_W_NaN))
parksDept[parksDept == 0] = np.mean(parksDept_W_NaN)

print np.mean(parksDept)
print np.median(parksDept)
print ((stats.mode(parksDept))[0])[0]

plt.boxplot(parksDept)
plt.ylabel("Parks and Recreation Department Water Usage")
plt.ylim([-300,15000])
plt.show()


# California Highway Patrol
highwayWaterUsage = (waterUse_DeptNames.loc[waterUse_DeptNames['Department Name'] == 'California Highway Patrol'])['Water Use (All Water Sources) (kgal)']
highwayDept = highwayWaterUsage.values

# find mean of array without NaN and replace NaN with mean and replace all zeros with mean
highwayDept_W_NaN = highwayDept[~(np.isnan(highwayDept))]
np.putmask(highwayDept, np.isnan(highwayDept), np.mean(highwayDept_W_NaN))
highwayDept[highwayDept == 0] = np.mean(highwayDept_W_NaN)

print np.mean(highwayDept)
print np.median(highwayDept)
print ((stats.mode(highwayDept))[0])[0]

plt.boxplot(highwayDept)
plt.ylabel("Highway Patrol Department Water Usage")
plt.ylim([-300,3000])
plt.show()


# California Military Department
militaryWaterUsage = (waterUse_DeptNames.loc[waterUse_DeptNames['Department Name'] == 'California Military Department'])['Water Use (All Water Sources) (kgal)']
militaryDept = militaryWaterUsage.values

# find mean of array without NaN and replace NaN with mean and replace all zeros with mean
militaryDept_W_NaN = militaryDept[~(np.isnan(militaryDept))]
np.putmask(militaryDept, np.isnan(militaryDept), np.mean(militaryDept_W_NaN))
militaryDept[militaryDept == 0] = np.mean(militaryDept_W_NaN)

print np.mean(militaryDept)
print np.median(militaryDept)
print ((stats.mode(militaryDept))[0])[0]

plt.boxplot(militaryDept)
plt.ylabel("Military Department Water Usage")
plt.ylim([-300,5000])
plt.show()