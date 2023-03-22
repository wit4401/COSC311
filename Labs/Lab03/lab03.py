"""
Lab 3: Basic One Dimensional Statistics
"""
# importing the necessary libraries
import stats
import pandas as pd
import matplotlib.pyplot as plt

bejaia = pd.read_csv('Bejaia_Region.csv')
sidi = pd.read_csv('Sidi-Bel_Abbes_Region.csv')

# Task 1: Mean values of the "Bejaia Region Dataset"

print('Mean values of Data Points in Bejaia Region Dataset:')
no_fire_means=[bejaia[bejaia['Classes']=='not fire']['RH'].mean(),bejaia[bejaia['Classes']=='not fire']['Ws'].mean(),
               bejaia[bejaia['Classes']=='not fire']['Temperature'].mean(),bejaia[bejaia['Classes']=='not fire']['Rain'].mean()]

fire_means=[bejaia[bejaia['Classes']=='fire']['RH'].mean(),bejaia[bejaia['Classes']=='fire']['Ws'].mean(),
            bejaia[bejaia['Classes']=='fire']['Temperature'].mean(),bejaia[bejaia['Classes']=='fire']['Rain'].mean()]

means_table=pd.DataFrame({'Fire':fire_means,'Not Fire':no_fire_means},index=['RH','Ws','Temp','Rain'])

print(means_table)

means_table.plot.bar()
plt.title('Mean Values of Data Point (Bejaia Region)')
plt.ylabel('mean')
plt.xlabel('value')
plt.show()

# Task 2: Using the " Sidi-Bel Abbes Region Dataset", calculate and show the median values of four attributes ("FFMC", "DMC", "DC" and "ISI", respectively)
print('\nMedians of Data Points in Sidi-Bel Dataset:')
print('FFMC:',sidi['FFMC'].median())
print('DMC:',sidi['DMC'].median())
print('DC:',sidi['DC'].median())
print('ISI:',sidi['ISI'].median())

# Task 3: Using the "Bejaia Region Dataset", calculate and show the 25-percent, 60-percent, and 75- percent quantiles of four attributes ("Temperature", "RH", "Ws" and "Rain", respectively)
print('\nQuartiles for Bejaia Region Data Points:')
print('Temperature:')
print('25% =',stats.quantile(list(bejaia['Temperature']),0.25))
print('60% =',stats.quantile(list(bejaia['Temperature']),0.6))
print('75% =',stats.quantile(list(bejaia['Temperature']),0.75),'\n')
print('Relative Humidity:')
print('25% =',stats.quantile(list(bejaia['RH']),0.25))
print('60% =',stats.quantile(list(bejaia['RH']),0.6))
print('75% =',stats.quantile(list(bejaia['RH']),0.75),'\n')
print('Wind Speed:')
print('25% =',stats.quantile(list(bejaia['Ws']),0.25))
print('60% =',stats.quantile(list(bejaia['Ws']),0.6))
print('75% =',stats.quantile(list(bejaia['Ws']),0.75),'\n')
print('Rain:')
print('25% =',stats.quantile(list(bejaia['Rain']),0.25))
print('60% =',stats.quantile(list(bejaia['Rain']),0.6))
print('75% =',stats.quantile(list(bejaia['Rain']),0.75),'\n')

# Task 4: Using the "Sidi-Bel Abbes Region Dataset", calculate and show the standard deviation values of four attributes ("Temperature", " Rain", "BUI" and "FWI", respectively) 
print('Standard Deviation for Sidi-Bel Abbes Region Data Points:')
print('Temperature:',stats.std(list(sidi['Temperature'])))
print('Rain:',stats.std(list(sidi['Rain'])))
print('BUI:',stats.std(list(sidi['BUI'])))
print('FWI:',stats.std(list(sidi['FWI'])))

# Task 5: Correlation between two attributes
print('\nCorrelation Coefficient between Relative Humidity and the Following Data Points in Bejaia Dataset:')
xs=list(bejaia['RH'])
print('Temperature:',stats.correlation(xs, list(bejaia['Temperature'])))
print('Ws:',stats.correlation(xs, list(bejaia['Ws'])))
print('Rain:',stats.correlation(xs, list(bejaia['Rain'])))
print('FFMC:',stats.correlation(xs, list(bejaia['FFMC'])))
print('DMC:',stats.correlation(xs,list(bejaia['DMC'])))
print('DC:',stats.correlation(xs, list(bejaia['DC'])))
print('ISI:',stats.correlation(xs,list(bejaia['ISI'])))
print('BUI:',stats.correlation(xs, list(bejaia['BUI'])))
print('FWI:',stats.correlation(xs, list(bejaia['FWI'])))

