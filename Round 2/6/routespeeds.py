import json
from pandas.io.json import json_normalize
from PIL import Image, ImageFont, ImageDraw
import math


# Function to convert latitude and longitude to tile coordinates of OpenStreetMap
def deg2num(lon_deg, lat_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


# Function to convert tile coordinates of OpenStreetMap to latitude and longitude at top left corner of the tile
def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lon_deg, lat_deg


# Using coordinates from exercise 5, get precise longitude and latitude from image corners and image size in coordinates
img_tile_start = deg2num(23.626, 61.5376, 13)  # Hardcoded
img_tile_end = deg2num(23.964, 61.4269, 13)  # Hardcoded
img_left_top = num2deg(img_tile_start[0], img_tile_start[1], 13)
img_right_bottom = num2deg(img_tile_end[0] + 1, img_tile_end[1] + 1, 13)
img_relative_size = [abs(img_left_top[0] - img_right_bottom[0]), abs(img_left_top[1] - img_right_bottom[1])]

# Open image and get absolute size in pixels
img = Image.open('tampere.png')
img_absolute_size = [img.width, img.height]


# This function calculates which pixel of the image corresponds to longitude and latitude coordinates
def point2pixels(lon, lat):
    x = (lon - img_left_top[0]) / img_relative_size[0] * img_absolute_size[0]
    y = -(lat - img_left_top[1]) / img_relative_size[1] * img_absolute_size[1]
    return int(x), int(y)


# Load json data from file,
with open('busdata.json') as data_file:
    data = json.load(data_file)
dfAll = json_normalize(data, 'body')
df = json_normalize(dfAll['monitoredVehicleJourney'])

# Get all of the spatial points and speeds recorded for a specific bus 'TKL_56'. This could have been parametrized...
bus_data = df[df['vehicleRef'] == 'TKL_56']
bus_data = bus_data[['vehicleLocation.latitude', 'vehicleLocation.longitude', 'speed']]

# Get default font and a drawing context
fnt = ImageFont.load_default()
draw = ImageDraw.Draw(img)


# Checks if the rectangles formed by two points of different sizes overlap
def overlap(point_a, size_a, point_b, size_b):
    end_a = [point_a[0] + size_a[0], point_a[1] + size_a[1]]
    end_b = [point_b[0] + size_b[0], point_b[1] + size_b[1]]
    if point_a[0] < end_b[0] and end_a[0] > point_b[0] and point_a[1] < end_b[1] and end_a[1] > point_b[1]:
        return True
    else:
        return False


last_drawn = 0
for i in range(bus_data.index.size):
    current_bus = bus_data.iloc[i]
    xy = point2pixels(float(current_bus['vehicleLocation.longitude']), float(current_bus['vehicleLocation.latitude']))
    size = draw.textsize(current_bus['speed'], font=fnt)
    if i > 0:  # For each point, compare if it overlaps with the previous one that was drawn. If not, draw new text.
        previous_bus = bus_data.iloc[last_drawn]
        p_xy = point2pixels(float(previous_bus['vehicleLocation.longitude']),
                            float(previous_bus['vehicleLocation.latitude']))
        p_size = draw.textsize(previous_bus['speed'], font=fnt)
        if xy[0] > 0 and xy[1] > 0 and not overlap(xy, size, p_xy, p_size):
            draw.text((xy[0], xy[1]), current_bus['speed'], font=fnt, fill=(0, 0, 0))
            last_drawn = i
    else:  # If is the first point
        draw.text((xy[0], xy[1]), current_bus['speed'], font=fnt, fill=(0, 0, 0))

# Saves final image
img.save('routespeeds.png')
