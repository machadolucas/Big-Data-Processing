Place your Python code into a file named **mapdata.py**. Also return an image file named **tampere.png** produced by your program.

[Openstreetmap](https://www.openstreetmap.org) is an open source map service whose goal is to provide a mapping service similar to e.g. Google maps but in a completely free manner. For example the map data can be freely downloaded from Openstreetmap (the only limitation is that the site should be credited as the source of the data).

Write a Python program that creates an image file in PNG format that shows the map of a region of interest using Openstreetmap's zoom level 13\. The "region of interest" is specified by the first four command line parameters, each of which is a decimal number: The first two give the latitude and longitude (that is, map coordinates) of the upper left (north-west) corner of the region of interest, and the latter two give the latitude and longitude of the lower right (east-south) corner. After these come a fifth command line parameter that specifies the name of the file into which the produced PNG fimage should be saved. For example running the program as **python 61.5376 23.626 61.4269 23.964 tampere.png** should produce a PNG image file **tampere.png** that contains a map covering roughly the whole city of Tampere.

In order to do this, your program needs to do the following steps:

1.  Download a set of map tiles (using zoom level 13) that covers the whole region of interest, whose upper left and lower right corner coordinates (latitude and longitude) are given by the first four command line parameters.
    *   Note: Openstreetmap provides map tiles in PNG format.
2.  Combine the individual map tiles into a single image.
3.  Store the resulting image into a file whose name is specified by the fifth command line parameter.

You need to return two files as your answer: the code file **mapdata.py** and a PNG image file **tampere.png** that your program creates when executed as mentioned in the example above. If your program works correctly, the latter image file should show a map of Tampere.

#### About downloading map (tiles) from Openstreetmap

Openstreetmap, as well as most other similar mapping sites, divide the map into small pieces (called tiles) that may be combined into a single larger map. This enhances the usability of mapping sites, as the map data can be downloaded little-by-little to the user's device instead of having to download a (possibly huge) complete map image at once.

It is in principle very easy to download individual map tiles from Openstreetmap: all one needs to do is access an URL with the right form. The Openstreetmap tiles server URLs are of form **tile.openstreetmap.org/ZOOM/X/Y.png**, where **ZOOM** is the zoom level and **X** and **Y** specify the map "coordinates" (which location in the world should the map show). For example if you visit the URL [tile.openstreetmap.org/13/4637/2309.png](http://tile.openstreetmap.org/13/4637/2309.png), you should see an Openstreetmap tile (a PNG image) with zoom level 13 of the area where the university of Tampere main campus is located.

So to download the tiles, it is enough to retrieve data from addresses of this form (e.g. by using [**urllib.request**](https://docs.python.org/3.6/library/urllib.request.html)). You can directly convert the downloaded PNG data into [a pillow Image object](http://pillow.readthedocs.io/en/4.3.x/reference/Image.html) by calling **Image.open(io.BytesIO(urllib.request.urlopen(url).read()))**, where **url** is a string that specifies the Openstreetmap tile address.

#### Some advice

Since  the "coordinates" **X** and **Y** used by Openstreetmap do not have a direct correspondence to normally used map coordinates, you need to do some calculations in order to know which tiles to load from Openstreetmap. The page [Slippy map tilenames](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) in the Openstreetmap wiki shows a ready implementation of a Python function **deg2num** that transforms map coordinates into the **X** and **Y** coordinates with a given zoom level. Use this function for both the upper left and lower right corner coordinates of the region that the completed map should cover: the results give you the range of **X** and **Y** values for which you need to fetch map tiles.

If you wonder how to combine several PNG tile images into a single complete map image, first create a new image e.g. as **completeMap = Image.new("RGB", (width, height))**, and then paste all individual tiles into it by calls of form **completeMap.paste(tile, (x, y))**, where **tile** is the tile image object to add, and **x**, **y** give the position into which the tile should be placed inside the whole map image.