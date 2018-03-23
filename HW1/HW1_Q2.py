import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


np.set_printoptions(threshold=np.inf)
data = pd.read_csv('./CAStateBuildingMetrics.csv')
deptNames_waterUse_electricUse = pd.DataFrame(data, columns=['Department Name', 'Water Use (All Water Sources) (kgal)', 'Electricity Use (kWh)'])


waterUsage = (deptNames_waterUse_electricUse['Water Use (All Water Sources) (kgal)']).values
electricityUsage = (deptNames_waterUse_electricUse['Electricity Use (kWh)']).values

waterUsage_W_NaN = waterUsage[~(np.isnan(waterUsage))]
np.putmask(waterUsage, np.isnan(waterUsage), np.mean(waterUsage_W_NaN))
waterUsage[waterUsage == 0] = np.mean(waterUsage_W_NaN)


electricityUsage_W_NaN = electricityUsage[~(np.isnan(electricityUsage))]
print np.mean(electricityUsage_W_NaN)
np.putmask(electricityUsage, np.isnan(electricityUsage), np.mean(electricityUsage_W_NaN))
electricityUsage[electricityUsage == 0] = np.mean(electricityUsage_W_NaN)


print stats.stats.pearsonr(waterUsage, electricityUsage)
## (0.66577579621732319, 5.2879953499989114e-221) ##
plt.scatter(waterUsage, electricityUsage)
plt.ylabel("Correlation between Water and Electricity use")
plt.show()


# Top 5 departments
# California Department of Transportation : 443
# California Department of Forestry and Fire Protection: 313
# Department of Parks and Recreation: 208
# California Highway Patrol: 107
# California Military Department: 103


## California Department of Transportation ##
transport_waterUse_electricUse = (deptNames_waterUse_electricUse.loc[deptNames_waterUse_electricUse['Department Name'] == 'California Department of Transportation'])
transport_waterUsage = transport_waterUse_electricUse['Water Use (All Water Sources) (kgal)'].values
transport_electricUsage = transport_waterUse_electricUse['Electricity Use (kWh)'].values
#Pearson Correlation and Scatter plot
print stats.stats.pearsonr(transport_waterUsage, transport_electricUsage)
## (0.55080708827781, 1.643219218327402e-36)
plt.scatter(transport_waterUsage, transport_electricUsage)
plt.ylabel("California Department of Transportation")
plt.show()


## California Department of Forestry and Fire Protection ##
forestry_waterUse_electricUse = (deptNames_waterUse_electricUse.loc[deptNames_waterUse_electricUse['Department Name'] == 'California Department of Forestry and Fire Protection'])
forestry_waterUsage = forestry_waterUse_electricUse['Water Use (All Water Sources) (kgal)'].values
forestry_electricUsage = forestry_waterUse_electricUse['Electricity Use (kWh)'].values
#Pearson Correlation and Scatter plot
print stats.stats.pearsonr(forestry_waterUsage, forestry_electricUsage)
## (0.22651218901438014, 5.2533111786498969e-05)
plt.scatter(forestry_waterUsage, forestry_electricUsage)
plt.ylabel("California Department of Forestry and Fire Protection")
plt.show()


## Department of Parks and Recreation ##
parks_waterUse_electricUse = (deptNames_waterUse_electricUse.loc[deptNames_waterUse_electricUse['Department Name'] == 'Department of Parks and Recreation'])
parks_waterUsage = parks_waterUse_electricUse['Water Use (All Water Sources) (kgal)'].values
parks_electricUsage = parks_waterUse_electricUse['Electricity Use (kWh)'].values
#Pearson Correlation and Scatter plot
print stats.stats.pearsonr(parks_waterUsage, parks_electricUsage)
## (0.15526842027669963, 0.025128797048117484)
plt.scatter(parks_waterUsage, parks_electricUsage)
plt.ylabel("Department of Parks and Recreation")
plt.show()


## California Highway Patrol ##
highway_waterUse_electricUse = (deptNames_waterUse_electricUse.loc[deptNames_waterUse_electricUse['Department Name'] == 'California Highway Patrol'])
highway_waterUsage = highway_waterUse_electricUse['Water Use (All Water Sources) (kgal)'].values
highway_electricUsage = highway_waterUse_electricUse['Electricity Use (kWh)'].values
#Pearson Correlation and Scatter plot
print stats.stats.pearsonr(highway_waterUsage, highway_electricUsage)
## (0.81679260770973405, 7.8385442993012886e-27)
plt.scatter(highway_waterUsage, highway_electricUsage)
plt.ylabel("California Highway Patrol")
plt.show()


## California Military Department
military_waterUse_electricUse = (deptNames_waterUse_electricUse.loc[deptNames_waterUse_electricUse['Department Name'] == 'California Military Department'])
military_waterUsage = military_waterUse_electricUse['Water Use (All Water Sources) (kgal)'].values
military_electricUsage = military_waterUse_electricUse['Electricity Use (kWh)'].values
#Pearson Correlation and Scatter plot
print stats.stats.pearsonr(military_waterUsage, military_electricUsage)
## (0.18718108469273598, 0.058322474537443166)
plt.scatter(military_waterUsage, military_electricUsage)
plt.ylabel("California Military Department")
plt.show()