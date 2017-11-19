import pandas as pd
import matplotlib.pyplot as plt

# First we read the tables, using [0] to get the first one in the page.
# Then we change country/territory column to 'Country'.
# After that, we remove notes from names with regex to avoid duplicates like 'Kosovo[8][9]' and 'Kosovo'.
# For byHappiness and byBirthRate, we skip rows for 'Europe' and 'World'.
# byBirthRate table has a two rows header and does not identify column names well, then we assign the names.

byGdp = \
    pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita',
                 attrs={'class': 'wikitable'},
                 header=0)[0]
byGdp = byGdp.rename(columns={'Country/Territory': 'Country'})
byGdp['Country'].replace(to_replace='\[[0-9a-zA-Z]*\]', value='', inplace=True, regex=True)

byHappiness = \
    pd.read_html('https://en.wikipedia.org/wiki/World_Happiness_Report', attrs={'class': 'wikitable'}, header=0,
                 skiprows=[43, 78])[0]
byHappiness['Country'].replace(to_replace='\[[0-9a-zA-Z]*\]', value='', inplace=True, regex=True)

byExpectancy = \
    pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy', attrs={'class': 'wikitable'},
                 header=0)[0]
byExpectancy['Country'].replace(to_replace='\[[0-9a-zA-Z]*\]', value='', inplace=True, regex=True)

byBirthRate = \
    pd.read_html('https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate',
                 attrs={'class': 'wikitable'}, header=0, skiprows=[1, 2])[0]
byBirthRate.columns = ['Country', 'WB2010 Rate‰', 'WB2010 Rank', 'OECD2011 Rate‰', 'OECD2011 Rank', 'CIA WF2013 Rate‰',
                       'CIA WF2013 Rank', 'CIA WF2014 Rate‰', 'CIA WF2014 Rank', 'CIA WF2016 Rate‰', 'CIA WF2016 Rank']
byBirthRate['Country'].replace(to_replace='\[[0-9a-zA-Z]*\]', value='', inplace=True, regex=True)

# Joins the dataframes to form the final one

joined = pd.merge(byGdp[['Country', 'Int$']], byHappiness[['Country', 'Score']], how='outer', on='Country')
joined = pd.merge(joined, byExpectancy[['Country', 'Both sexes life expectancy']], how='outer', on='Country')
joined = pd.merge(joined, byBirthRate[['Country', 'CIA WF2016 Rate‰']], how='outer', on='Country')
joined.columns = ['country names', 'GDP (PPP) per capita', 'Happiness score', 'Life expectancy', 'Birth rate']
joined = joined.set_index('country names')

# Saves html file

outputFile = open('countrydata.html', 'w', encoding='utf-8')
outputFile.write(joined.to_html())
outputFile.close()

# Creates figure and subplots.
# Here we do some customizations: Figure size and dpi, padding in layout, and size of markers.

plt.figure(figsize=(10, 7), dpi=90, tight_layout=True)

plt.subplot(321)
plt.scatter(joined['GDP (PPP) per capita'], joined['Happiness score'], s=1)
plt.title('GDP vs happiness')

plt.subplot(322)
plt.scatter(joined['GDP (PPP) per capita'], joined['Life expectancy'], s=1)
plt.title('GDP vs life expectancy')

plt.subplot(323)
plt.scatter(joined['GDP (PPP) per capita'], joined['Birth rate'], s=1)
plt.title('GDP vs birth rate')

plt.subplot(324)
plt.scatter(joined['Happiness score'], joined['Life expectancy'], s=1)
plt.title('happiness vs life expectancy')

plt.subplot(325)
plt.scatter(joined['Happiness score'], joined['Birth rate'], s=1)
plt.title('happiness vs birth rate')

plt.subplot(326)
plt.scatter(joined['Life expectancy'], joined['Birth rate'], s=1)
plt.title('life expectancy vs birth rate')

# Saves the figure

plt.savefig('countryplots.png')
