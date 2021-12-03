import arcpy
from arcpy.sa import *
    print("PRISM_ppt_stable_4kmM3_"+str(i)+"_asc.asc")
    out=ZonalStatisticsAsTable("globalwatershed","FID","PRISM_ppt_stable_4kmM3_"+str(i)+"_asc.asc",(r"C:\Users\taohuang\Documents\Tao\Data\PRISM\table"+str(i)+".dbf"))
    



