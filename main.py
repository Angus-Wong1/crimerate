import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib

#matplotlib.use('TkAgg')
# Load GeoJSON file
gdf = gpd.read_file('zipcodes.json')

# Plot the GeoDataFrame
gdf.plot()

# Show the plot
#plt.savefig('test.png')
plt.show()
