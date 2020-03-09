# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 01:19:02 2020

@author: Sayantan
"""

import pandas
from geopy.geocoders import ArcGIS

def modify_data(file):
    df=pandas.read_csv(file)
    nom=ArcGIS()
    df["Address"]=df["Address"]+","+df["City"]+","+df["State"]+","+df["Country"]
    df["Coordinates"]=df["Address"].apply(nom.geocode)
    df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x!=None else None)
    df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x!=None else None)
    return df

    