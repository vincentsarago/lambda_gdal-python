#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ctypes import cdll

#Import other Modules

path = os.path.dirname(os.path.realpath(__file__))
os.environ['GDAL_DATA'] = os.path.join(path, "local/share/gdal")
lib2 = cdll.LoadLibrary(os.path.join(path, 'local/lib/libproj.so.9'))
lib1 = cdll.LoadLibrary(os.path.join(path, 'local/lib/libgdal.so'))
from osgeo import gdal, ogr, osr

#Import gdal modules
from osgeo import gdal

def processing_func(event, context):
    "This is my worker function that responds to an API getaway call"
    
    sceneid = event['scene']
    
    try:
        WRSPath = sceneid[3:6]
        WRSRow = sceneid[6:9]
        landsat_address = 'http://landsat-pds.s3.amazonaws.com/L8/{0}/{1}/{2}/{2}'.format(WRSPath, WRSRow, sceneid)

        bqa = '/vsicurl/{0}_BQA.TIF'.format(landsat_address)
        meta_file = '{0}_MTL.txt'.format(landsat_address)
        try:
            meta_data = urllib2.urlopen(meta_file).readlines()
        except:
            return {'errorMessage': 'Landsat image {} not available on aws'.format(sceneid)}

        src_ds = gdal.Open(bqa, gdal.GA_ReadOnly)
        geoT = src_ds.GetGeoTransform()
        proj = src_ds.GetProjection()
        
        cols = master_ds.RasterXSize    
        rows = master_ds.RasterYSize
    
        src_ds = None

        return {'landsatid': sceneid, 'xsize': cols, 'ysize': rows}
    except:
        return {'errorMessage': 'Could not open image {}'.format(sceneid)}
