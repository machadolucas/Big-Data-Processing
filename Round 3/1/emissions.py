import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize

# Some parameters used later. Adjust figure size and grid.
start_year = 1990
end_year = 2030

fig = plt.figure(figsize=(12, 6), dpi=160, tight_layout=True)
ax = fig.add_subplot(111)
ax.grid(color='xkcd:light grey', linestyle='-', linewidth=0.5, zorder=-999)

# Reads csv file, filter only passenger cars (types M1 and M1G)).
# Drops rows with NaN in ensirekisterointipvm column, and convert its values to int after cutting the year from date.
# Then drops vehicles with NaN values for Co2 emissions.
df = pd.read_csv('Tieliikenne AvoinData 4.10.csv', sep=';', encoding='latin1', low_memory=False, header=0)
df = df[df['ajoneuvoluokka'].isin(['M1', 'M1G'])]
df = df.dropna(subset=['ensirekisterointipvm'])
df['ensirekisterointipvm'] = pd.to_numeric(df['ensirekisterointipvm'].apply(lambda x: x[:4]), downcast='integer')
df = df.dropna(subset=['Co2'])

# Creates the pivot table with 'average'(CO2 g/km) and 'len'(count) columns of cars by year of registration.
table = pd.pivot_table(df, index=['ensirekisterointipvm'], values=['Co2'], aggfunc=[np.average, len])

# Plot scatter values
years_labels = np.array(table.index)
average_values = np.array([x[0] for x in table['average'].values])
ax.scatter(years_labels, average_values, label='Data', c=(0, 0, 0), s=6, zorder=999)

# Linear regression
years_from_zero = np.array(
    [x - start_year for x in list(table.index)])  # 1990 is 0, 1991 is 1... Only years present in table.
all_years_labels = np.array(range(start_year, end_year + 1))  # 1990,1991,1992...
all_years_from_zero = np.array(range(0, end_year - start_year + 1))  # 0,1,2,3...
slope, intercept, r_value, p_value, std_err = stats.linregress(years_from_zero, average_values)
ax.plot(all_years_labels, intercept + slope * all_years_from_zero, 'r', label='Linear regression')

# Polynomial regression
p3 = np.poly1d(np.polyfit(years_labels, average_values, 3))
p7 = np.poly1d(np.polyfit(years_labels, average_values, 7))
p11 = np.poly1d(np.polyfit(years_labels, average_values, 11))
x_space = np.linspace(start_year, end_year, 100)
ax.plot(x_space, p3(x_space), '--', label='Polynomial order 3')
ax.plot(x_space, p7(x_space), '-.', label='Polynomial order 7')
ax.plot(x_space, p11(x_space), ':', label='Polynomial order 11')


# Non-linear regression for all the years
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


initial_guess = [0, 0, 0]
popt, pcov = optimize.curve_fit(func, years_from_zero, average_values, p0=initial_guess)
x_space_from_zero = np.linspace(0, end_year - start_year, 100)
ax.plot(x_space, func(x_space_from_zero, *popt), '--', label='Non-linear')

# Non-linear regression between 2008-2017
popt2, pcov2 = optimize.curve_fit(func, years_from_zero[15:], average_values[15:], p0=initial_guess)
ax.plot(x_space, func(x_space_from_zero, *popt2), '-.', label='Non-linear 2008-2017')

# Print values for years 2005, 2010, 2015
for x, y in zip([2005, 2010, 2015], [table.loc[2005][0], table.loc[2010][0], table.loc[2015][0]]):
    ax.annotate(str(round(y, 2)), xy=(x, y))

# Print values estimated for years 2020, 2025, 2030
nl_all_values = [func(30, *popt), func(35, *popt), func(40, *popt)]
for x, y in zip([2020, 2025, 2030], nl_all_values):
    ax.annotate(str(round(y, 2)), xy=(x, y))

nl_late_values = [func(30, *popt2), func(35, *popt2), func(40, *popt2)]
for x, y in zip([2020, 2025, 2030], nl_late_values):
    ax.annotate(str(round(y, 2)), xy=(x, y))

# Finalize plotting
ax.set_ylim(0, 240)
ax.legend()
plt.title('Average CO2 per year (g/km)')
plt.savefig('emissions.png')
