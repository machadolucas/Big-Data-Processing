Place your Python code into a file named **htmldata.py**. In addition return the files **countrydata.html** and **countryplots.png** created by your program.

Internet pages as such are a common source of data. But since web pages typically contain also a lot of extra information, such as free form text or low level html code, we need  to do some preprocessing in order to gather (only) the data that we are interested in. In this question we concentrate on data that is stored within html tables. The pandas library contains a handy [**read_html**](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html#pandas.read_html) function for retrieving such data.

Write a Python program that:

1.  Reads the first html table from each of the following Wikipedia pages into a pandas DataFrame:
    *   [List of countries by GDP (PPP) per capita](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita)
    *   [World Happiness Report](https://en.wikipedia.org/wiki/World_Happiness_Report)
    *   [List of countries by life expectancy](https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy)
    *   [List of sovereign states and dependent territories by birth rate](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate)
2.  Creates from the data of the read tables a new pandas DataFrame that has the following structure:
    *   Row labels (index): country names.
    *   Columns: "GDP (PPP) per capita", "Happiness score", "Life expectancy" and "Birth rate".
    *   When populating the columns, select the values from "Both sexes life expectancy" for life expectancy and the values under the title "CIA WF 2016" for birth rate.
3.  Writes the DataFrame created in step 2 into a html file called **countrydata.html** using the DataFrame member function [**to_html**](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html).
4.  Creates 6 matplotlib scatter plots that depict dependencies (or lack of) between any two of the four attributes present in the table from step 2.
    *   The six pairings are (1) GDP vs happiness, (2) GDP vs life expectancy, (3) GDP vs birth rate, (4) happiness vs life expectancy, (5) happiness vs birth rate and (6) life expectancy vs birth rate.
    *   For each pairing the scatter plot consists of points (x, y) for all countries in the data, where x corresponds to the first attribute of the pair and y to the second attribute. E.g. the first plot would have GDP per capita on the x-axis and happiness score on the y-axis.
    *   Include the 6 scatter plots as subplots into the same matplotlib figure and save the figure into the file **countryplots.png**.
        *   E.g. the [Scatter star poly example](https://matplotlib.org/gallery/lines_bars_and_markers/scatter_star_poly.html) shows how to plot 6 subplots. But perhaps you might want to use different sizes or symbols.
        *   Use [the savefig function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html?highlight=savefig#matplotlib.pyplot.savefig) to save the plot as a png image. You do not need to specify the file type; it should be enough to specify the filename as "countryplots.png".