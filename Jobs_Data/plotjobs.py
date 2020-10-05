# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:45:08 2020

@author: gonzr
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Found this colour scheme online
CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'
# Add the colours to matplotlib
color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,CB91_Purple, CB91_Violet]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

# Read the csv file ignoring all the spaces
df = pd.read_csv("jobs.csv",sep="\s*[,]\s*")
# Set the dates to be in the datetime format in pandas
df["Date Applied"] = pd.to_datetime(df["Date Applied"], format="%d/%m/%Y")
df["Date Rejected"] = pd.to_datetime(df["Date Rejected"], format="%d/%m/%Y")

# Pull the data about rejected offers and their dates sorted by week from the dataset
rejected = df["Rejected"] == True
rejected = df[rejected]
week_rejected = df['Date Rejected'].groupby(df['Date Rejected'].dt.week).count()#Count number of rejections per week
week_rejected= week_rejected.to_frame()
week_rejected = week_rejected.rename(columns={"Date Rejected": "Jobs Rejected"})#Week numbers
# Pull the data about job applications and their dates sorted by week from the dataset
week_groups = df['Date Applied'].groupby(df['Date Applied'].dt.week).count()#COunt number of applications per week
week_groups = week_groups.to_frame()
week_groups = week_groups.rename(columns={"Date Applied": "Jobs Applied"})
week_groups = week_groups.rename_axis('Week')#Week numbers
#Start the figure and define the width of the bars
fig, ax = plt.subplots(figsize = (12,7.5))
width = 0.4
# Plot the data
ax.bar(week_groups.index-0.2, week_groups["Jobs Applied"],align='center',width=width)
ax.bar(week_rejected.index+0.2, week_rejected['Jobs Rejected'], color='r',width=width)
# Set labels and title
ax.set_title('Jobs applied per week', fontsize=20)
ax.set_xlabel('Date',fontsize=20)
ax.set_ylabel('Job applications',fontsize=20)
xsticks = np.arange(24,40,1)
ax.set_xticks(xsticks)
plt.yticks(fontsize=15)
weeknames = ['June','June','June', 'July','July','July','July','August','August','August','August','Sept','Sept','Sept','Sept', 'Oct']
ax.set_xticklabels(weeknames)
plt.xticks(rotation=45)
ax.autoscale_view()
ax.legend(('Applied', 'Rejected'))
plt.show()


