import arcpy


arcpy.SpatialJoin_analysis("usgs_wt_ID","S_USA.NorWeST_PredictedStreams","USGS_nearest","JOIN_ONE_TO_ONE","KEEP_ALL","#","CLOSEST")

