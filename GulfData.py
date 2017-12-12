from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np

data = pd.read_csv('Cruise.csv')

data = data.query('Depth <= 650 and Cruise == 1')

lats = data['Latitude']
longs = data['Longitude']


m = Basemap(resolution='l',lat_0=lats.mean(),lon_0=longs.mean(), projection='merc',
           llcrnrlon=-100, llcrnrlat=10, urcrnrlon=-80, urcrnrlat=30)


x, y = m(longs.values,lats.values)


means = data.groupby(['Station']).mean()
cods = means['COD']
longs = means['Longitude']
lats = means['Latitude']
silicates = means['Silicate']
phosphates = means['Phosphate']
nits = means['Nits']
pda = means['PDA']
oxygen = means['Oxygen']
salinity = means['Salinity']
temperatures = means['Temperature']
means.shape


x,y = m(longs.values,lats.values)
m.scatter(x, y, c=cods, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='COD [µM]')
plt.show()


m.scatter(x, y, c=nits, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Nitrato+Nitrito [µM]')
plt.show()


m.scatter(x, y, c=phosphates, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Fosfato [µM]')
plt.show()


m.scatter(x, y, c=oxygen, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Oxígeno [ml/l]')
plt.show()


m.scatter(x, y, c=pda, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Potential Density Anomaly  [kg/m-3]')
plt.show()


m.scatter(x, y, c=silicates, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Silicato [µM]')
plt.show()


m.scatter(x, y, c=salinity, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Salinidad')
plt.show()


m.scatter(x, y, c=temperatures, cmap='afmhot')
m.bluemarble()
m.colorbar(location='bottom', label='Temperatura [°C]')
plt.show()

subdata = data[['Salinity', 'COD', 'Nits', 'Phosphate','Temperature','Oxygen','Silicate','PDA', 'BottomDepth','Depth']]
pd.plotting.scatter_matrix(subdata, alpha = 0.2, figsize = (10,10), diagonal = 'kde');
plt.show()


import seaborn as sns

f, ax = plt.subplots(figsize=(10, 8))
corr = subdata.corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
plt.show()



