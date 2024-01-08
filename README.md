# GEOG485 Final Project: Spatial Density-Based Clustering Tool for Botanical Seed Collections

<b>Project Description: Spatial Density-Based Clustering Tool for Botanical Seed Collections</b><br>

The Spatial Density-Based Clustering Tool for Botanical Seed Collections is a custom script tool developed for the exploration and analysis of spatial patterns within botanical seed collection data. This project leverages the power of ArcPy and ArcGIS to convert tabular data containing coordinates into a point feature class, facilitating subsequent density-based clustering analysis. By applying Density-Based Clustering (DBSCAN) to the geographic distribution of botanical seed collections, the tool provides valuable insights into spatial concentrations, enabling researchers to identify significant patterns in the data.

<b>Key features:</b>

<b>1. Customized Script Tool:</b> The tool is designed as an ArcGIS script tool, providing an intuitive interface for users to input parameters and execute the analysis. This user-friendly approach enhances accessibility for researchers, even those with limited programming experience.

<b>2. Coordinate Data Conversion:</b> The script tool converts coordinate points stored in an Excel table (provided as input) into a point feature class. This process utilizes the XYTableToPoint tool, generating a spatial representation of botanical seed collection locations.

<b>3. Spatial Density-Based Clustering:</b> The core functionality of the tool involves applying Density-Based Clustering to the newly created point feature class. This analysis reveals spatial clusters of seed collections, aiding researchers in identifying regions with high concentrations of botanical diversity.

<b>4. Parameter Customization:</b> Users have the flexibility to customize key parameters for the clustering analysis, including the clustering method (DBSCAN), minimum feature cluster size, search distance, and time interval. This adaptability allows researchers to fine-tune the analysis based on the characteristics of their dataset.

<b>5. Spatial Reference Support:</b> The tool supports a spatial reference system with a specific focus on the commonly used WGS 1984 coordinate system (EPSG:4326). This ensures compatibility with a wide range of geographic datasets and promotes consistency in spatial analysis.

<b>6. Error Handling:</b> Robust error-handling mechanisms are implemented in the script to provide informative messages in case of execution errors. This feature helps users troubleshoot issues and ensures the tool's reliability.

<b>Main Usage:</b>

<b>1. Input Data:</b> Users provide an Excel table containing coordinate points of botanical seed collections. The tool expects fields representing longitude (X_LONG) and latitude (Y_LAT).

<b>2. Spatial Clustering Analysis:</b> The tool creates a point feature class from the input coordinates and applies Density-Based Clustering to unveil spatial patterns. Users can customize clustering parameters such as method, minimum feature cluster size, search distance, and time interval.

<b>3. Output:</b> The output of the tool includes a point feature class representing the spatial distribution of botanical seed collections and a clustered feature class highlighting significant spatial clusters.

Overall, the Spatial Density-Based Clustering Tool for Botanical Seed Collections is a valuable resource for researchers and ecologists interested in understanding the spatial dynamics of seed collection patterns. By combining the capabilities of ArcPy with customizable clustering parameters, this tool facilitates the exploration and visualization of spatial data, contributing to a deeper understanding of botanical biodiversity distribution.

![image](https://github.com/bec-in-tech/GEOG485-Final-Project/assets/120440399/0adcbb5e-8ecf-4651-8046-0b97f412cf84)
