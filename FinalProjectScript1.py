#-------------------------------------------------------------------------------
# Name:        Density-Based Clustering of Data Points
# Project:     GEOG-485 Final Project
# Author:      Rebecca Ubalde
# Created:     10/14/2023
#-------------------------------------------------------------------------------

import arcpy

try:
    # Set up the workspace and file paths
    arcpy.env.workspace = r"C:\PSU\Geog485_FA23\FinalProject\FinalProject\FinalProject.gdb"
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    arcpy.env.overwriteOutput = True

    # Define the input Excel table file
    inputTable = r"C:\PSU\Geog485_FA23\FinalProject\FinalProject\Collection_Data_Clean.xlsx\Collections$"

    # Define the output point feature class
    outputFC = "Collect_Points"

    # Define the long and lat (X & Y) field names from the input table
    x_Coord = "X_LONG"
    y_Coord = "Y_LAT"

    # Use XYTableToPoint tool to create the point shapefile
    arcpy.management.XYTableToPoint(inputTable, outputFC, x_Coord, y_Coord)

    print(f"Point feature class was successfully created with a spatial reference of 4326.")

    # Define the parameters for the Density-Based Clustering
    inFeatures = outputFC
    outFeatures = "Collect_DBC"
    clusterMethod = "DBSCAN"
    minFeatCluster = 2
    searchDistance = "5 Miles"
    timeField = "COLL_DT"
    searchTimeInterval = "15 Years"

    # Perform Density-Based Clustering analysis
    arcpy.stats.DensityBasedClustering(inFeatures, outFeatures, clusterMethod, minFeatCluster, searchDistance, "", timeField, searchTimeInterval)

    print("Success: Density-based clustering applied.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

except Exception as e:
    print(e)

