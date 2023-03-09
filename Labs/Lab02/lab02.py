"""
Task 1: Using the pandas package
"""
import pandas as pd #import pandas python package

sidi = pd.read_csv("Sidi-Bel_Abbes_Region.csv",header=[0])
bejaia = pd.read_csv("Bejaia_Region.csv",header=[0])

# Part I
print("Sidi-Bel Region Info:")
sidi.info()

print("\nBejaia Region Info:")
bejaia.info()

# Part II
print("\nSidi-Bel Region describe():")
print(sidi.describe())

print("\nBejaia Region describe():")
print(bejaia.describe())

# Part III
print("\nUnique Ws values (Sidi-Bel):")
print(*sidi['Ws'].unique())

print("\nUnique Ws values (Bejaia):")
print(*bejaia['Ws'].unique())

# Part IV
print("\nData Points in Bejaia Region Data:")
for name,lst in bejaia.items():
    print("# values in " + name + ": " + str(len(lst)))

print("\nData Points in the Sidi Region Data:")
for name,lst in sidi.items():
    print("# values in " + name + ": " + str(len(lst)))
"""
Task 2: draw a line figure to show the temperature change with time for the "Bejaia Region Dataset"
"""
import matplotlib.pyplot as plt

plt.figure(figsize=(7,8))
for month in bejaia['month'].unique(): 
    plt.plot(bejaia[bejaia['month']==month]['day'],bejaia[bejaia['month']==month]['Temperature'],label='Month '+str(month))
plt.xlabel("Day")
plt.ylabel("Temperature (Celcius)")
plt.title('Temperature Change Through the Month for Each Month(Bejaia Region)')
plt.legend()

"""
Task 3: draw a scatterplot figure to show the relationship between the temperature and the Fire Weather Index (FWI) for the "Sidi-Bel Abbes Region Dataset"
"""
plt.figure(figsize=(7,8))
plt.scatter(sidi['FWI'],sidi['Temperature'])
plt.xlabel('Fire Weather Index')
plt.ylabel('Temperature')
plt.title('Scatterplot of FWI and Temperature (Sidi-Bel Abbes Region)')


"""
Task 4: draw a histogram to show the average Relative Humidity (RH) for each month for the "Bejaia Region Dataset"
"""
plt.figure(figsize=(7,8))
bejaia.groupby(['month'])['RH'].mean().plot.hist()
plt.xlabel('Average')
plt.ylabel('Frequency')
plt.title('Average Relative Humidity (Bejaia Region)')


"""
Task 5: draw a bar figure to show the maximum Rain amount in a day for each month for the "Bejaia Region Dataset"
"""
plt.figure(figsize=(7,8))
plt.bar([month for month in bejaia['month'].unique()],[bejaia[bejaia['month']==month]['Rain'].max() for month in bejaia['month'].unique()])
plt.xlabel("Month")
plt.ylabel('Maximum Rainfall')
plt.title("Maximum Rainfall in a Day for Each Month (Bejaia Region)")

"""
Task 6: draw a histogram to show the Wind speed (Ws) distribution in 5 bins for the "Sidi-Bel Abbes Region Dataset" in June, 2012
"""
plt.figure(figsize=(7,8))
plt.hist([sidi[(sidi['month']==6) & (sidi['year']==2012)]['Ws']],bins=5)
plt.xlabel("Wind Speed")
plt.ylabel("Frequency")
plt.title('Wind Speed Distribution (Sidi-Bel Abbes Region)')

"""
Task 7: draw a line figure to show the correlation between temperature (Temp) and Relative Humidity (RH) for the "Sidi-Bel Abbes Region Dataset" in July, 2012
"""
plt.figure(figsize=(7,8))
plt.plot(sidi[(sidi['month']==7) & (sidi['year']==2012)]['Temperature'],sidi[(sidi['month']==7) & (sidi['year']==2012)]['RH'])
plt.xlabel('Temperature')
plt.ylabel('Relative Humidity')
plt.title('Relationship between Temperature and Relative Humidity')

"""
Task 8: draw a bar figure to show the distribution of Relative Humidity (RH) for the "Bejaia Region Dataset". The x-axis is the decile of Relative Humidity (20s, 30s, ..., 90s), and y-axis is the number of days
"""
from collections import Counter
plt.figure(figsize=(7,8))
plt.bar(bejaia['RH'].unique(),list(Counter(bejaia['RH']).keys()))
plt.xlabel('Relative Humidity')
plt.ylabel('# of days')
plt.title('Distribution of Relative Humidity Based on # of Days (Bejaia Region)')

"""
Task 9: draw a figure (any type you want) to show the average temperature for each month when there is "no fire" and there is "fire" for the "Bejaia Region Dataset"
"""
avgs=list(bejaia.groupby(['month','Classes'])['RH'].mean())

fire_dict={'Fire':[avgs[i] for i in range(len(avgs)) if i%2==0],
           'Not Fire':[avgs[i] for i in range(len(avgs)) if i%2==1]}
new_df=pd.DataFrame(fire_dict,index=['Jun','Jul','Aug','Sept'])
new_df.plot.bar()

plt.xlabel('Status of Fire')
plt.ylabel('Average Temperature')
plt.title("Average Temperature Each Month Based on Fires")
plt.savefig('task9.png')
plt.show()