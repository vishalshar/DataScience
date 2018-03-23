# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
import scipy.spatial.distance as distc
from collections import Counter


data = pd.read_csv('./CAStateBuildingMetrics.csv')
subData_prop = pd.DataFrame(data, columns=['Department Name','City', 'Primary Property Type', 'Property Area(ft²)'])
dept_names = subData_prop['Department Name']
#print len(Counter(dept_names))  ##37

city_names = subData_prop['City']
#print len(Counter(city_names))  ##847

prop_type_names = subData_prop['Primary Property Type']
#print len(Counter(prop_type_names))  ##1722

prop_area_names = subData_prop['Property Area(ft²)']
#print len(Counter(prop_area_names))  ##1557

subData_resource = pd.DataFrame(data, columns=['Property Name','Electricity Use (kWh)','Natural Gas Use (therms)', 'Propane Use (kBtu)', 'Water Use (All Water Sources) (kgal)','Site Energy Use (kBtu)'])
electricityUse = subData_resource['Electricity Use (kWh)']
naturalGas = subData_resource['Natural Gas Use (therms)']
propaneUse = subData_resource['Propane Use (kBtu)']
waterUse = subData_resource['Water Use (All Water Sources) (kgal)']
siteEnergy = subData_resource['Site Energy Use (kBtu)']

electricityUse_wNaN = electricityUse[~(np.isnan(electricityUse))]
naturalGas_wNaN = naturalGas[~(np.isnan(naturalGas))]
propaneUse_wNaN = propaneUse[~(np.isnan(propaneUse))]
waterUse_wNaN = waterUse[~(np.isnan(waterUse))]
siteEnergy_wNaN = siteEnergy[~(np.isnan(siteEnergy))]

electricityMean = np.mean(electricityUse_wNaN)
naturalGasMean = np.mean(naturalGas_wNaN)
propaneUseMean = np.mean(propaneUse_wNaN)
waterUseMean = np.mean(waterUse_wNaN)
siteEnergyMean = np.mean(siteEnergy_wNaN)
# print electricityMean, naturalGasMean, propaneUseMean, waterUseMean, siteEnergyMean

build1_mendotaMainStation = (subData_resource.loc[subData_resource['Property Name'] == 'METROPOLITAN STATE HOSPITAL'])
build1_mendota_electric = build1_mendotaMainStation['Electricity Use (kWh)'].values[0]
build1_mendota_natural = build1_mendotaMainStation['Natural Gas Use (therms)'].values[0]
build1_mendota_propane = build1_mendotaMainStation['Propane Use (kBtu)'].values[0]
build1_mendota_water = build1_mendotaMainStation['Water Use (All Water Sources) (kgal)'].values[0]
build1_mendota_energy = build1_mendotaMainStation['Site Energy Use (kBtu)'].values[0]
values = [build1_mendota_electric, build1_mendota_natural, build1_mendota_propane, build1_mendota_water, build1_mendota_energy]
print values

## Similarity function using Euclidean, Manhattan and Cosine
## Find similarity of below
for index, row in subData_resource.iterrows():
    if(row['Property Name'] == 'LONG BEACH FIELD OFFICE'):
        continue
    electricity = row['Electricity Use (kWh)']
    naturalGas = row['Natural Gas Use (therms)']
    propaneUse = row['Propane Use (kBtu)']
    waterUse = row['Water Use (All Water Sources) (kgal)']
    energyUse = row['Site Energy Use (kBtu)']
    if(math.isnan(electricity)):
        electricity = electricityMean
    if(math.isnan(naturalGas)):
        naturalGas = naturalGasMean
    if(math.isnan(propaneUse)):
        propaneUse = propaneUseMean
    if(math.isnan(waterUse)):
        waterUse = waterUseMean
    if(math.isnan(energyUse)):
        energyUse = siteEnergyMean
    manhattanDist = distc.cityblock([electricity,naturalGas,propaneUse,waterUse,energyUse],values)
    #print manhattanDist,"\\",row['Property Name']
    euclideanDist = distc.euclidean([electricity,naturalGas,propaneUse,waterUse,energyUse],values)
    #print euclideanDist,"\\", row['Property Name']
    cosineDist = distc.cosine([electricity,naturalGas,propaneUse,waterUse,energyUse],values)
    # print cosineDist,"\\", row['Property Name']
