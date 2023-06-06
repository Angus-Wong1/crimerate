import folium
import geopandas as gpd

# Load GeoJSON file
gdf = gpd.read_file('zipcodes.json')

# Ensure data is in correct projection
gdf = gdf.to_crs('EPSG:4326')

# Calculate the center of the map
x_map_center = gdf.geometry.centroid.x.mean()
y_map_center = gdf.geometry.centroid.y.mean()

# Create a map centered at the centroid of your data
m = folium.Map(location=[y_map_center, x_map_center], zoom_start=13)

# Add GeoJSON to map
folium.GeoJson(gdf).add_to(m)

# Save the map
m.save('ol.html')
