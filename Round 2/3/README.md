Place your Python code into a file named <span style="font-weight: bold;">vehstats.py</span>. Also return a file named **vehstats.png** created by your program.

Write a Python program that:

1.  Reads in the vechicle data available for download in CSV format from [Open data at Trafi](https://www.trafi.fi/en/information_services/open_data).
2.  Creates four [piecharts](https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html) with matplotlib into the same figure and saves the figure as **vehstats.png**. The four piecharts should show:
    1.  The shares of the 5 most common car brands, with the remaining brands grouped together under a single title "others".
    2.  The shares of cars that have been driven:
        *   0-50000 km
        *   50001-100000 km
        *   100000-150000 km
        *   150000-200000 km
        *   200000-250000 km
        *   250000-300000 km
        *   \> 300000 km
    3.  The shares of cars that are:
        *   ≤ 5 years old
        *   \> 5 but ≤ 10 years old
        *   \> 10 but ≤ 15 years old
        *   \>15 but ≤ 20 years old
        *   \> 20 years old
    4.  The shares of cars whose CO<sub>2</sub> emissions are:
        *   ≤ 100 g/km
        *   \> 100 but ≤ 125 g/km
        *   \> 125 but ≤ 150 g/km
        *   \> 150 but ≤ 175 g/km
        *   \> 175 but ≤ 200 g/km
        *   \> 200 but ≤ 225 g/km
        *   \> 225 but ≤ 250 g/km
        *   \> 250 g/km

Consider only normal passenger cars. The column "ajoneuvoluokka" of the data describes the type of the vehicle: passenger cars have the vehicle type code "M1" or "M1G".

Further helpful information about the vehicle data (for non-Finnish students):

*   The column "merkkiSelvakielinen" gives the brand name (e.g. "Mercedes-Benz", "Toyota", and so on).
*   The column "matkamittarilukema" gives the amount of kilometers driven by the car (until the time the car was last inspected).
*   The column "ensirekisterointipvm" gives the date when the car was first registered. Use this to calculate an estimate about how old the car is.
*   The column "Co2" gives the CO<sub>2</sub> emissions of the car as g/km.