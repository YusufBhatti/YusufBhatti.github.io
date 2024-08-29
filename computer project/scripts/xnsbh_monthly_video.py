#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:28:58 2019

@author: ee18yb (Yusuf Bhatti)
"""

"""
Read in netcdf files and read in AOD

"""

### Import modules ###

import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.colors as mcolors
import cartopy.feature as cfeature
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap, cm
from matplotlib.dates import date2num
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num, date2index
import os
import glob
import imageio


### Read in and define netcdf files of monthly 10 Tg SO2 progression ###
### by defining the directory pathway ###
expname='xnsbh'

### Loop through the directory and obtain all the files ###
files = sorted(glob.glob('E://Data Files (NetCDF)/xnsbh/Monthly_AOD/*.nc'))

###################################################################################
######################### Extracting the data for the plots #######################
###################################################################################

### Looping the variables needed to be extracted for the different months ###
for file in files:
    vn=Dataset(file)
    lon       = vn.variables['longitude'][:]
    lat      = vn.variables['latitude'][:]
    time      = vn.variables['t'][:]
    Ait_Ins0 = vn.variables['AITKEN_MODE__INSOL__STRATO_AOD'][:]
    Ait_Sol0 = vn.variables['AITKEN_MODE__SOLUBLE__STRATO__AOD'][:]
    Coa_Ins0 = vn.variables['COARSE_MODE__INSOL__STRATO_AOD'][:]
    Coa_Sol0 = vn.variables['COARSE_MODE__SOLUBLE__STRATO_AOD'][:]
    Acc_Ins0 = vn.variables['ACCUM_MODE__INSOL__STRATO_AOD'][:]
    Acc_Sol0 = vn.variables['ACCUM_MODE__SOLUBLE__STRATO_AOD'][:]
    
    
### Add up all components [above] to get an overall aod ###
    aod       = Ait_Ins0+Ait_Sol0+Coa_Ins0+Coa_Sol0+Acc_Ins0+Acc_Sol0
    print(np.shape(aod))
    
### Extract the second dimension to obtain the ###
    aod550=np.squeeze(aod[:,2,:,:])
    print(np.shape(aod550))

### Set the time and date of each plots ####
    t_unit="days since 2000-09-01T00:00:00Z"
    #t_cal =  vn1.variables[tname].calendar
    t_cal =  "360_day"

    dates =num2date(time,units=t_unit,calendar=t_cal)
    print(dates)
    ntime=len(time)


### Creating map variables ###
    import  matplotlib
    
### set the font size globally to get the ticklabels big ###
    matplotlib.rcParams['font.sans-serif'] = "Arial"
    matplotlib.rcParams['font.family'] = "sans-serif"

    label_size=14
    mpl.rcParams['xtick.labelsize'] =label_size
    mpl.rcParams['ytick.labelsize'] =label_size

    plt.rc('grid', color = 'black')
    plt.rc('grid', alpha = 0.3) # alpha is percentage of transparency
    
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18
    
###################################################################################
###################### Ploting models for the Months ##############################
###################################################################################

### Create a figure for each plot with the same size ### 
    fig = plt.figure(figsize=(15.745,15), edgecolor='w')
    
#### Setting up a [Mercator] projection with the focus at 180 W and ####
################ coarse resoltuion coastlines ##########################
    map = Basemap(llcrnrlon=0.,llcrnrlat=-80,urcrnrlon=358.,urcrnrlat=85,
            projection='cyl',resolution ='c')
 
### Add coastline features ###
    map.drawcoastlines(linewidth=0.75)  # Draw coastlines and 
    map.drawcountries(linewidth=0.75)   # countries
    
### organise the longitude and latitude using meshgrid ###
    lons, lats = np.meshgrid(lon, lat)
    
### Define x and y as Longitude and Latitude ###
    x, y = map(lons, lats)

#### Plotting Latitude and Longitude grid every 30 degrees ####
    meridians = np.arange(0.,360,30.)    
    parallels = np.arange(-90.,90,30.)
    map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=12)  
    map.drawparallels(parallels,labels=[1,0,0,0],fontsize=12)

### Set the axis ###
    clevs=np.arange(0+0.025,0.55+0.025,0.025)
    
### Change values outside contour limits to min and max contours limits
    aod550[aod550 > 0.55] = 0.525
    
###################################################################################
################################## Construct the plot #############################
###################################################################################
    
    cs = map.contourf(x,y,aod550,clevs,cmap='jet',linewidths=1.)
    
### Add colourbar ###
    cbar = map.colorbar(cs,location='bottom',pad="5%")
    cbar.set_label('stratospheric AOD',fontsize=18)
    sdate=str(dates[0])
    
### Add title ###
    plt.title("10 Tg SO$_2$ @ 21-23 km height"+" ("+sdate[0:10]+")",fontsize=20)
    
### Save and display the plot ###
    plt.savefig("E://Model_Plots/xnsbh/monthly_video/" +expname+"_"+sdate[0:10]+".png",bbox_inches = 'tight')

###############################################################
########## Create a GIF of all the daily plots ################
###############################################################

### Define the location of directory ###   
png_dir = 'E://Model_Plots/xnsbh/monthly_video/'
images = []

### Loop all the .png files in that directroy ###
for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
        
### Set the duration of each plot image for the GIF ###
kargs = { 'duration': 0.2 }

### Create and Save the GIF plot ###
imageio.mimsave('E://Model_Plots/xnsbh/monthly_video/monthly_10.gif', images,**kargs)