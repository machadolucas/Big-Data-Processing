Place your Python code into a file named **routespeeds.py**. Also return an image file named **routespeeds.png** produced by your program.

Implement a Python program that receives as input the PNG map image of the Tampere region and bus location data file (from question 3), and then augments the map image with speed values for some bus vehicle in the data. The speed values are plotted to map locations that correspond to the coordinates where the speed information was recorded.

The speed values should be plotted in such manner that they do not overlap: when you plot a speed value, record the location of the map. Then when you consider the next point (coordinates and speed), plot the speed only if it would not overlap with the previously written speed value.

#### Some advice

One problem concerns about how to draw text to a PNG image. For this it should be helpful to look into [the ImageDraw module](http://pillow.readthedocs.io/en/4.3.x/reference/ImageDraw.html) of the [pillow library](http://pillow.readthedocs.io). Note that the function **draw.text** requires a font. You can access a default font by doing something like **fnt = ImageFont.load_default()**.

Another question concerns how to detect if speed value texts overlap. You may check the size (width and height of a bounding box, that is, a rectangle that fits over the text as tightly as possible) of some text by using the function **draw.textsize**. This enables you to avoid plotting overlapping speed values: if the bounding box of the current speed value would overlap the bounding box of the previously plotted speed value, skip plotting the current speed value.