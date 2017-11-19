import io
import sys
import math
import urllib.request
from PIL import Image

# Get command line parameters
lat_start = float(sys.argv[1])
lon_start = float(sys.argv[2])
lat_end = float(sys.argv[3])
lon_end = float(sys.argv[4])
output_filename = sys.argv[5]


# Function to convert latitude and longitude to tile coordinates of OpenStreetMap
def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


# Get OpenStreetMap coordinates and a range of tile ids to download
coord_start = deg2num(lat_start, lon_start, 13)
coord_end = deg2num(lat_end, lon_end, 13)
range_x = list(range(coord_start[0], coord_end[0] + 1))
range_y = list(range(coord_start[1], coord_end[1] + 1))

# Creates the complete image, and fill it with tiles
completeMap = Image.new("RGB", (256 * len(range_x), 256 * len(range_y)))
for index_x, x in enumerate(range_x):
    for index_y, y in enumerate(range_y):
        url = 'http://tile.openstreetmap.org/13/' + str(x) + '/' + str(y) + '.png'
        tile = Image.open(io.BytesIO(urllib.request.urlopen(url).read()))
        completeMap.paste(tile, (256 * index_x, 256 * index_y))

# Saves final complete image
completeMap.save(output_filename)
