import arcpy
from arcpy import env
from arcpy.sa import *

import arcpy
for yr in xrange(2014,2021):
     input="PRISM_tmean_stable_4kmM3_"+str(yr)+"08_asc.asc"
     output=r"C:\Users\taohuang\Documents\Tao\Data\PRISM\temp"+str(yr)
     ExtractValuesToPoints("usgs_wt_ID",input,output,"NONE","VALUE_ONLY")
     
