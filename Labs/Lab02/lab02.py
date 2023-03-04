# COSC Lab 02

"""
Task 1: Using the  pandas package
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

"""
Task 2: draw a line figure to show the temperature change with time for the "Bejaia Region Dataset"
"""
import matplotlib.pyplot as plt

plt.plot(bejaia['day'],bejaia['Temperature'])
plt.xlabel("day")
plt.ylabel("Temperature")
plt.show()
"""
Task 3: draw a scatterplot figure to show the relationship between the temperature and the Fire Weather Index (FWI) for the "Sidi-Bel Abbes Region Dataset"
"""
plt.scatter(sidi['FWI'],sidi['Temperature'])
plt.show()

"""
Task 4: draw a histogram to show the average Relative Humidity (RH) for each month for the "Bejaia Region Dataset"
"""

"""
Task 5: draw a bar figure to show the maximum Rain amount in a day for each month for the "Bejaia Region Dataset"
"""

"""
Task 6: draw a histogram to show the Wind speed (Ws) distribution in 5 bins for the "Sidi-Bel Abbes Region Dataset" in June, 2012
"""

"""
Task 7: draw a line figure to show the correlation between temperature (Temp) and Relative Humidity (RH) for the "Sidi-Bel Abbes Region Dataset" in July, 2012
"""

"""
Task 8: draw a bar figure to show the distribution of Relative Humidity (RH) for the "Bejaia Region Dataset". The x-axis is the decile of Relative Humidity (20s, 30s, ..., 90s), and y-axis is the number of days
"""

"""
Task 9: draw a figure (any type you want) to show the average temperature for each month when there is "no fire" and there is "fire" for the "Bejaia Region Dataset"
"""