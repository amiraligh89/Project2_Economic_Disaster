import sys
import json
import csv 
import os
import pandas as pd

data_folder = os.path.join('Data')
map_folder = os.path.join('test_map')

def create_geojson(year,yr):
    
  # Create references to the files we will read in and the file we will output
  xlsfile = os.path.join(data_folder,f'laucnty{yr}.xlsx')
  jsonfile = os.path.join(data_folder,f'cb_{year}_us_county_20m.json')
  geojsonfile = os.path.join(map_folder,f'CountiesPlusUnemp{year}.geojson')

  # Read the unemployment data from excel and create a dataframe.
  xl = pd.ExcelFile(xlsfile)
  df = xl.parse(f"laucnty{yr}")

  # Rename the columns to be more useful. 
  df.columns = ['a', 'STATEFP','COUNTYFP','FullCountyName','Year','b','LaborForce','Employed','Unemployed','UnemploymentRate']

  # keep only lines that are data entries, not title lines or blanks
  df = df.loc[df["Year"]==f"{year}",:]

  # separate the state from the county name
  # new data frame with split value columns 
  new = df["FullCountyName"].str.split(",", n = 1, expand = True) 
  
  # making separate last name column from new data frame 
  df["StateAbbr"]= new[1] 
  
  # Dropping old Name columns 
  df.drop(columns =['a','b',"FullCountyName",'Year'], inplace = True) 
  
  # Create blank dictionaries that will be come the employment data and the final geojson
  geojson = {}
  empdata = {}

  # Loop through the dataframe and add information to the empdata dictionary. 
  # We will use this to put these values into the geojson.
  for row, rowvals in df.iterrows():
        
    # pull information from dataframe into temporary variables
    STATEFP = rowvals[0]
    COUNTYFP = rowvals[1]
    LaborForce = rowvals[2]
    Employed = rowvals[3]
    Unemployed = rowvals[4]
    UnemploymentRate = rowvals[5]    
    StateAbbr = rowvals[6]
            
    # Check to see if this state/county has already been added to the dictionary.
    # If not, then add an entry for it.
    if STATEFP not in empdata:
        empdata[STATEFP]={}
        
    # Append the data for this county to its entry in the dictionary
    empdata[STATEFP][COUNTYFP]={
        "LaborForce": LaborForce,
        "Employed": Employed,
        "Unemployed": Unemployed,
        "UnemploymentRate": UnemploymentRate,
        "StateAbbr": StateAbbr
    }
    
  # Open up the existing geojson file and read it into the empty geojson dictionary created above.
  # While reading it in, pull the matching state and county fips from the empdata dictionary so we can add the unemployment info to the geojson.
  with open(jsonfile, 'r') as f:
    geojson = json.load(f)
    for feature in geojson['features']:
      featureProperties = feature['properties']
      statefp = featureProperties['STATEFP']
      countyfp = featureProperties['COUNTYFP']
      featureData = empdata.get(statefp).get(countyfp, {})
      for key in featureData.keys():
        featureProperties[key] = featureData[key]

  # Output this updated geojson.
  with open(geojsonfile, 'w') as f:
    json.dump(geojson, f)

# Run the function for 2013 through 2018
create_geojson(2013,13)
create_geojson(2014,14)
create_geojson(2015,15)
create_geojson(2016,16)
create_geojson(2017,17)
create_geojson(2018,18)