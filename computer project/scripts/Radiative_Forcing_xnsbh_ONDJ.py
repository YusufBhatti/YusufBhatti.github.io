# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:53:47 2019

@author: ee18yb - Yusuf Bhatti
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
import matplotlib.gridspec as gridspec
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap, cm
from matplotlib.dates import date2num
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num, date2index


# Read in and define netcdf files of monthly 10 Tg SO2 progression

expname='xnsbh'
pname='xnsbg'

mnames=['0oct','0nov','0dec','1jan','1feb','1mar','1apr',
        '1may','1jun','1jul','1aug','1sep','1oct','1nov']
#mnames=['1feb','1apr','1jun','1aug']
inpath = 'E://Data Files (NetCDF)/'+expname+'/Radiative_Forcing/'
path = 'E://Data Files (NetCDF)/'+pname+'/Radiative_Forcing/'

###############################################################
########### Extracting the data for the plots #################
###############################################################
### Looping the variables needed to be extracted for the different months ###

fig, axes = plt.subplots(nrows=7, ncols=2, sharex=True, figsize=(15.745,15))
fig.subplots_adjust(hspace=0.3, wspace=-0.58)
for ax,name in zip(axes.flat, mnames):
    infile= inpath+expname+'a_pd200'+name+'TOAradfluxesMDSJamesB.nc'
    nfile= path+pname+'a_pd200'+name+'TOAradfluxesMDSJamesB.nc'
    vn=Dataset(infile)
    v=Dataset(nfile)
    lon       = vn.variables['longitude'][:]
    lat      = vn.variables['latitude'][:]
    time      = vn.variables['t'][:]
    OUT_LW = vn.variables['OUTGOING_LW_RAD_FLUX__TOA_'][:] # Extract perturbed strat
    OUT_SW = vn.variables['OUTGOING_SW_RAD_FLUX__TOA_'][:]
    O_LW = v.variables['OUTGOING_LW_RAD_FLUX__TOA_'][:] # Extract normal strat
    O_SW = v.variables['OUTGOING_SW_RAD_FLUX__TOA_'][:]

    
### Add up all aod components to get overall aod ###
    print(np.shape(OUT_LW))
    print(np.shape(O_LW))

### Squeeze the array to extract the values into 2D ###
    LW=np.squeeze(OUT_LW[:,:,:,:])
    SW=np.squeeze(OUT_SW[:,:,:,:])
    OLW=np.squeeze(O_LW[:,:,:,:])
    OSW=np.squeeze(O_SW[:,:,:,:])

### Define the total outgoing radative forcing for the xsnbh/g ###
    Rad=LW+SW
    ORad=OLW+OSW

### Define the difference to calculate the total radiative forcing effects ###
    Diff=ORad-Rad
    print(np.max(Diff))
    print(np.min(Diff))

### Calculate and define the mean radiative forcing difference ###
    Diff_Mean = np.mean(Diff)
    print(Diff_Mean)
    t_unit="days since 2000-09-01T00:00:00Z"
    #t_cal =  vn1.variables[tname].calendar
    t_cal =  "360_day"

    dates =num2date(time,units=t_unit,calendar=t_cal)
    print(dates)
    ntime=len(time)

### Creating map variables ###

    import  matplotlib
### set the font size globally to get the ticklabels big too:

    matplotlib.rcParams['font.sans-serif'] = "Arial"
    matplotlib.rcParams['font.family'] = "sans-serif"

    label_size=5
    mpl.rcParams['xtick.labelsize'] =label_size
    mpl.rcParams['ytick.labelsize'] =label_size

    plt.rc('grid', color = 'black')
    plt.rc('grid', alpha = 0.3) # alpha is percentage of transparency
    
    plt.rcParams['xtick.labelsize'] = 5
    plt.rcParams['ytick.labelsize'] = 5
    
###########################################################################
######### Ploting for the Oct 2000, Nov 2000, Dec 2000, Jan 2001 ##########
###########################################################################

#### Setting up a [Mercator] projection with the focus at 180 W and ####
#### low resoltuion coastlines #########################################
    map_ax = Basemap(llcrnrlon=0.,llcrnrlat=-80,urcrnrlon=358.,urcrnrlat=85,
            projection='cyl',resolution ='c',ax=ax)
    map_ax.drawcoastlines()

### organise the longitude and latitude using meshgrid ###
    lons, lats = np.meshgrid(lon, lat)
### Define x and y as Longitude and Latitude ###
    x, y = map_ax(lons, lats) 
    
### Plotting Latitude and Longitude grid every 30 and 60 degrees, respectively ###
    meridians = np.arange(0.,360,60.)    
    parallels = np.arange(-90.,90,30.)
    map_ax.drawmeridians(meridians,labels=[0,0,0,1],fontsize=6)  
    map_ax.drawparallels(parallels,labels=[1,0,0,0],fontsize=6)

###################################################################################
################################## Construct the plot #############################
###################################################################################
### Set the axis ###
    clevs=np.arange(-90,90+5,5)

### Change values outside contour limits to min and max contours limits ###
    Diff[Diff > 90] = 90
    Diff[Diff < -90] = -90

### define the plot and use contourf ###
    cs = ax.contourf(lon,lat,Diff,clevs,cmap='seismic')
### Add colourbar ###

### Add colourbar ###
    cbar = map_ax.colorbar(cs,location='right',pad="5%")
    cbar.set_label('W/m$^2$',fontsize=5)
    sdate=str(dates[0])

### Add title with the looped dates ###
    plt.title("Radiative Forcing 10 Tg SO$_2$ @ 21-23 km height"+" ("+sdate[0:7]+")",fontsize=7)
    
### Add the global radiation values to the plot with 2 decimal points
### GMOR = Global Mean Outgoing Radiation
    ax.text(15,-78,'GMOR = '+ str(round(Diff_Mean,2))+ 'W/m$^{2}$',fontsize=6)



### Save and display the plot as a .png and save in high quality (dpi=600) ###
    plt.savefig("E://Model_Plots/RF_Comparison_all.png",dpi=600,bbox_inches = 'tight')