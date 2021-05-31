from mpl_toolkits.basemap import Basemap
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('Meteorite-Landings.csv')
df['Year'] = pd.to_datetime(df['year'], format='%d/%m/%Y %I:%M:%S %p', errors='coerce').dt.year
df = df.fillna(0)
df = df.astype(int, errors='ignore')
df = df.query('reclat != 0 and reclong != 0')

mass_series = df['mass (g)']
df['mass'] = mass_series

cols = df.columns.tolist
cols = ['name', 'id', 'nametype', 'mass', 'recclass', 'fall', 'Year', 'reclat',
       'reclong', 'GeoLocation']
df = df[cols]

df['scale'] = np.floor(np.log10(df['mass']))

fell_df = df.query('fall == "Fell"')

lats = df['reclat']
longs = df['reclong']

map = Basemap(projection='cea', lat_0= lats.min())
map.drawcoastlines(linewidth=0.5)




plt.title('Incidência de Meteoritos')
map.scatter(lats, longs, latlon=True, s=5*df['scale'])

plt.show()