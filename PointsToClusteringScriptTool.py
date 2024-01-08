import arcpy

try:
    # Set up the workspace
    workspace = arcpy.GetParameterAsText(0)
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True

    # Input Parameters
    inputTable = arcpy.GetParameterAsText(1)
    outputFC = arcpy.GetParameterAsText(2)
    x_Coord = "X_LONG"
    y_Coord = "Y_LAT"
    spatialRef = arcpy.SpatialReference(4326)

    # Create point feature class
    arcpy.management.XYTableToPoint(
        inputTable,
        outputFC,
        x_Coord,
        y_Coord,
        "",
        spatialRef)

    arcpy.AddMessage(f"Point feature class '{outputFC}' was successfully created.")

    # Use the newly created output feature class as input for clustering
    inFeatures = outputFC
    outFeatures = arcpy.GetParameterAsText(3)
    clusterMethod = arcpy.GetParameterAsText(4)
    minFeatCluster = arcpy.GetParameter(5)
    searchDistance = arcpy.GetParameterAsText(6)
    timeField = arcpy.GetParameterAsText(7)
    searchTimeInterval = arcpy.GetParameterAsText(8)

    # Perform Density-Based Clustering analysis
    arcpy.stats.DensityBasedClustering(
        inFeatures,
        outFeatures,
        clusterMethod,
        minFeatCluster,
        searchDistance,
        "",
        timeField,
        searchTimeInterval)

    arcpy.AddMessage("Density-based clustering was successfully executed.")

except arcpy.ExecuteError:
    arcpy.AddError(arcpy.GetMessages(2))

except Exception as e:
    arcpy.AddError(str(e))

