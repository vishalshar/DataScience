# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
import scipy.spatial.distance as distc
from collections import Counter


data = pd.read_csv('./CAStateBuildingMetrics.csv')
subData_prop = pd.DataFrame(data, columns=['Property Name','Department Name','City', 'Primary Property Type ', 'Property Area(ft²)', 'Electricity Use (kWh)','Natural Gas Use (therms)', 'Propane Use (kBtu)', 'Water Use (All Water Sources) (kgal)','Site Energy Use (kBtu)'])
dept_names = subData_prop['Department Name']
city_names = subData_prop['City']
prop_type_names = subData_prop['Primary Property Type ']
prop_area = subData_prop['Property Area(ft²)']

electricityUse = subData_prop['Electricity Use (kWh)']
naturalGas = subData_prop['Natural Gas Use (therms)']
propaneUse = subData_prop['Propane Use (kBtu)']
waterUse = subData_prop['Water Use (All Water Sources) (kgal)']
siteEnergy = subData_prop['Site Energy Use (kBtu)']

# Removing NaN and calculating Mean
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

##Clean Property area
prop_area_wNaN = prop_area[~(np.isnan(prop_area))]
prop_area_mean = np.mean(prop_area_wNaN)


## Transformation matrix
city_transformations = {}
dept_transformations = {}
prop_type_transformations = {}

## Create transformation matrix
i = 1
for row in Counter(dept_names).most_common():
    dept_transformations[row[0]] = i
    i+=1


#print dept_transformations
i = 1
for row in Counter(city_names).most_common():
    city_transformations[row[0]] = i
    i+=1


#print city_transformations
i = 1
for row in Counter(prop_type_names).most_common():
    prop_type_transformations[row[0]] = i
    i+=1


building_data = (subData_prop.loc[subData_prop['Property Name'] == 'MENDOTA MAINTENANCE STATION'])
build_name = dept_transformations[building_data['Department Name'].values[0]]
build_city = city_transformations[building_data['City'].values[0]]
build_prop_type = prop_type_transformations[building_data['Primary Property Type '].values[0]]
build_prop_area = building_data['Property Area(ft²)'].values[0]
build_electric = building_data['Electricity Use (kWh)'].values[0]
build_natural = building_data['Natural Gas Use (therms)'].values[0]
build_propane = propaneUseMean#building_data['Propane Use (kBtu)'].values[0]
build_water = building_data['Water Use (All Water Sources) (kgal)'].values[0]
build_energy = building_data['Site Energy Use (kBtu)'].values[0]

if(math.isnan(build_prop_area)):
    build_prop_area = prop_area_mean
values = [build_name, build_city, build_prop_type, build_prop_area, build_electric, build_natural, build_propane, build_water, build_energy]

print values


for index, row in subData_prop.iterrows():
    name = dept_transformations[row['Department Name']]
    city = city_transformations[row['City']]
    prop_type = prop_type_transformations[row['Primary Property Type ']]
    prop_area = row['Property Area(ft²)']
    electricity = row['Electricity Use (kWh)']
    naturalGas = row['Natural Gas Use (therms)']
    propaneUse = row['Propane Use (kBtu)']
    waterUse = row['Water Use (All Water Sources) (kgal)']
    energyUse = row['Site Energy Use (kBtu)']
    if(math.isnan(prop_area)):
        prop_area = prop_area_mean
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
    testMatrix = [name, city, prop_type, prop_area, electricity, naturalGas, propaneUse, waterUse, energyUse]
    #print name, city, prop_type, prop_area, electricity, naturalGas, propaneUse, waterUse, energyUse
    manhattanDist = distc.cityblock(testMatrix, values)
    #print manhattanDist,"\\",row['Property Name']
    euclideanDist = distc.euclidean(testMatrix, values)
    #print euclideanDist,"\\", row['Property Name']
    cosineDist = distc.cosine(testMatrix, values)
    print cosineDist, "\\", row['Property Name']