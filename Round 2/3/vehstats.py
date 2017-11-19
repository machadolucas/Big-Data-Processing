import pandas as pd
import matplotlib.pyplot as plt

# Reads csv file, filter only passenger cars (types M1 and M1G)).
# Interprets ensirekisterointipvm column as date format. Set figure size.

df = pd.read_csv('Tieliikenne AvoinData 4.10.csv', sep=';', encoding='latin1', low_memory=False, header=0)
df = df[df['ajoneuvoluokka'].isin(['M1', 'M1G'])]
df['ensirekisterointipvm'] = pd.to_datetime(df['ensirekisterointipvm'], format='%Y-%m-%d', errors='ignore')

plt.figure(figsize=(8, 8), dpi=160, tight_layout=True)

# Get number of vehicles by five most popular brands, and sum 'Others' amount.
# Then plots the pie chart

brands = df['merkkiSelvakielinen'].value_counts()
firstFiveBrands = brands[:5]
otherBrandsSum = brands[5:].sum()

plt.subplot(221)
plt.pie(firstFiveBrands.tolist() + [otherBrandsSum], labels=firstFiveBrands.index.tolist() + ['Others'],
        autopct='%1.1f%%')
plt.title('Brands')

# Get number of vehicles by kilometers driven, ignoring vehicles with NaN values.
# Then plots the pie chart

kilometers = df['matkamittarilukema'].dropna(axis=0)
km0to50 = kilometers[(kilometers <= 50000)].index.size
km50to100 = kilometers[(kilometers > 50000) & (kilometers <= 100000)].index.size
km100to150 = kilometers[(kilometers > 100000) & (kilometers <= 150000)].index.size
km150to200 = kilometers[(kilometers > 150000) & (kilometers <= 200000)].index.size
km200to250 = kilometers[(kilometers > 200000) & (kilometers <= 250000)].index.size
km250to300 = kilometers[(kilometers > 250000) & (kilometers <= 300000)].index.size
km300orMore = kilometers[(kilometers > 300000)].index.size

kmsLabels = '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '>300'
kms = [km0to50, km50to100, km100to150, km150to200, km200to250, km250to300, km300orMore]

plt.subplot(222)
plt.pie(kms, labels=kmsLabels, autopct='%1.1f%%')
plt.title('Mileage (1000 Km)')

# Get number of vehicles by age, relative to exercise submission date (20171113).
# Then plots the pie chart

yearsLessThan5 = df[(df['ensirekisterointipvm'] >= pd.to_datetime('20121113', format='%Y%m%d'))].index.size
years5to10 = df[(df['ensirekisterointipvm'] < pd.to_datetime('20121113', format='%Y%m%d')) & (
    df['ensirekisterointipvm'] >= pd.to_datetime('20071113', format='%Y%m%d'))].index.size
years10to15 = df[(df['ensirekisterointipvm'] < pd.to_datetime('20071113', format='%Y%m%d')) & (
    df['ensirekisterointipvm'] >= pd.to_datetime('20021113', format='%Y%m%d'))].index.size
years15to20 = df[(df['ensirekisterointipvm'] < pd.to_datetime('20021113', format='%Y%m%d')) & (
    df['ensirekisterointipvm'] >= pd.to_datetime('19971113', format='%Y%m%d'))].index.size
yearsMoreThan20 = df[(df['ensirekisterointipvm'] < pd.to_datetime('19971113', format='%Y%m%d'))].index.size

yearsLabels = '≤5', '5-10', '10-15', '15-20', '>20'
years = [yearsLessThan5, years5to10, years10to15, years15to20, yearsMoreThan20]

plt.subplot(223)
plt.pie(years, labels=yearsLabels, autopct='%1.1f%%')
plt.title('Age (years)')

# Get number of vehicles by CO2 emissions, ignoring vehicles with NaN values.
# Then plots the pie chart

co2 = df['Co2'].dropna(axis=0)
co2_to100 = co2[(co2 <= 100)].index.size
co2_100to125 = co2[(co2 > 100) & (co2 <= 125)].index.size
co2_125to150 = co2[(co2 > 125) & (co2 <= 150)].index.size
co2_150to175 = co2[(co2 > 150) & (co2 <= 175)].index.size
co2_175to200 = co2[(co2 > 175) & (co2 <= 200)].index.size
co2_200to225 = co2[(co2 > 200) & (co2 <= 225)].index.size
co2_225to250 = co2[(co2 > 225) & (co2 <= 250)].index.size
co2_moreThan250 = co2[(co2 > 250)].index.size

emissionsLabels = ['≤100', '100-125', '125-150', '150-175', '175-200', '200-225', '225-250', '>250']
emissions = [co2_to100, co2_100to125, co2_125to150, co2_150to175, co2_175to200, co2_200to225, co2_225to250,
             co2_moreThan250]

plt.subplot(224)
plt.pie(emissions, labels=emissionsLabels, autopct='%1.1f%%')
plt.title('CO2 emissions (g/km)')

# Saves the figure

plt.subplots_adjust(bottom=0.3, right=0.7, top=0.7, left=0.3, wspace=1, hspace=1)
plt.savefig('vehstats.png')
