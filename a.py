import pandas as pd
import matplotlib.pyplot as plt
 
us_baby_names = pd.read_csv("US_BaBy_Names.csv", header=0)
 
title = "The bar char illustrates the ratio of men and women from 2004 to 2014"
male_data, female_data = [[us_baby_names[(us_baby_names.Year == year) & (us_baby_names.Gender == gender)].Gender.count()
                           for year in range(2004, 2015)] for gender in ('M','F')]

plt.bar(range(2004, 2015), male_data, color='blue', width=0.35, label ='Male')
plt.bar([i+0.35 for i in range(2004, 2015)], female_data, color='pink', width=0.35, label ='Female')
plt.xlabel('Year')
plt.ylabel('Number of babies')
plt.title(title)
plt.xticks([r+0.17 for r in range(2004, 2015)], range(2004, 2015))
plt.legend()
plt.show()