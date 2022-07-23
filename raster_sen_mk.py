# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 23:57:03 2022

@author: shiyulu
"""


import numpy as np
import pymannkendall as mk
from osgeo import gdal
import sys
import time
#import skimage as img


def Read_img2array(img_file_path):

    dataset = gdal.Open(img_file_path) 
    print('total_Bands：', dataset.RasterCount)
   
    if dataset is None:
        print('Unable to open *.tif')
        sys.exit(1)  
    #projection = dataset.GetProjection()
    #geotrans = dataset.GetGeoTransform()
    im_width = dataset.RasterXSize 
    im_height = dataset.RasterYSize 
    im_bands = dataset.RasterCount 
    img_array = dataset.ReadAsArray()
    return im_width,im_height,im_bands,img_array


width,height,bands,dataset= Read_img2array('aohi_def.tif')

#set up
trends=np.full((height,width),"")
slopes=np.full((height,width),0.0)



dic={'increasing':1,'decreasing':-1,'no trend':0}


for i in range(height):

    t=time.time()
    for j in range(width):
        
        data=dataset[:,i,j]
       
        trend, h, p, z, Tau, s, var_s, slope, intercept = mk.original_test(data)
       
        trends[i,j]=dic[trend]
        slopes[i,j]=slope
    t1=time.time()
    print (t1-t)



#trendsArray = np.array(trends)
