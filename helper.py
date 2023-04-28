import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import streamlit


def fetch_locationwise(d1,location):
    locate_d1=d1
    if location == 'Overall':
        temp_d1 = locate_d1
    if location != 'Overall':
        temp_d1 = locate_d1[locate_d1['Locality'] == location]

    x = temp_d1.groupby('Locality').sum()[
        ['MURDER', 'ATTEMPT TO MURDER', 'CULPABLE HOMICIDE NOT AMOUNTING TO MURDER', 'KIDNAPPING & ABDUCTION',
         'ROBBERY', 'BURGLARY', 'THEFT', 'RIOTS', 'CHEATING', 'HURT/GREVIOUS HURT', 'DOWRY DEATHS']].sort_values(
        'MURDER', ascending=False).reset_index()
    return x

def location_list(d1):
    location = d1['Locality'].unique().tolist()
    location.sort()
    location.insert(0, 'Overall')
    return location

def fetch_female(d2, year, locality):
    fetch_d2 = d2
    # flag = 0
    if year == 'Overall' and locality == 'Overall':
        temp_d2 = fetch_d2
    if year == 'Overall' and locality != 'Overall':
        # flag = 1
        temp_d2 = fetch_d2[fetch_d2['Locality'] == locality]
    if year != 'Overall' and locality == 'Overall':
        temp_d2 = fetch_d2[fetch_d2['Year'] == int(year)]
    if year != 'Overall' and locality != 'Overall':
        temp_d2 = fetch_d2[(fetch_d2['Year'] == year) & (fetch_d2['Locality'] == locality)]

    x = temp_d2.groupby('Locality').sum()[['Year', 'Rape', 'Kidnapping and Abduction', 'Dowry Deaths',
                                            'Assault on women with intent to outrage her modesty',
                                            'Insult to modesty of Women', 'Cruelty by Husband or his Relatives',
                                            'Importation of Girls']].sort_values('Rape', ascending=False).reset_index()

    # if flag == 1:
    #     x = temp_d2.groupby('Year').sum()[['Year','Rape','Kidnapping and Abduction','Dowry Deaths','Assault on women with intent to outrage her modesty','Insult to modesty of Women','Cruelty by Husband or his Relatives','Importation of Girls']].sort_values('Year').reset_index()
    # else:
    #     x = temp_d2.groupby('Loocality').sum()[['Year','Rape','Kidnapping and Abduction','Dowry Deaths','Assault on women with intent to outrage her modesty','Insult to modesty of Women','Cruelty by Husband or his Relatives','Importation of Girls']].sort_values('Rape',ascending=False).reset_index()

    # x['Year'] = x['Year'].astype('int')

    return x


# def female(d2):
#     female = d2.groupby('Loocality').sum()[['Rape']].sort_values('Rape',ascending=False).reset_index()
#
#     return female

def locality_year_list(d2):
    years = d2['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    locality = np.unique(d2['Locality'].dropna().values).tolist()
    locality.sort()
    locality.insert(0, 'Overall')

    return years,locality


def total_crimes(d1):
    d1.rename(columns={'Locality': 'Locality', 'TOTAL IPC CRIMES': 'Total Crimes'}, inplace=True)
    return d1

def juvenile(d3):
    d3.rename(columns={'Crime Head': 'Crimes', 'Cases Reported against Juveniles ': 'Cases Reported against Juveniles'}, inplace=True)
    # x['Total']=x['16 Years & Above and below 18 Years-Boys']+x['16 Years & Above and below 18 Years-Girls']
    return d3


# def abc(d1):
#
#     plt.rcParams['figure.figsize'] = [20, 10]
#     plt.plot(d1['Locality'], d1['MURDER'], label='MURDER')
#     plt.plot(d1['Locality'], d1['ATTEMPT TO MURDER'], label='ATTEMPT TO MURDER')
#     plt.plot(d1['Locality'], d1['CULPABLE HOMICIDE NOT AMOUNTING TO MURDER'],
#              label='CULPABLE HOMICIDE NOT AMOUNTING TO MURDER')
#     plt.plot(d1['Locality'], d1['RAPE'], label='RAPE')
#     plt.plot(d1['Locality'], d1['CUSTODIAL RAPE'], label='CUSTODIAL RAPE')
#     plt.plot(d1['Locality'], d1['KIDNAPPING & ABDUCTION'], label='KIDNAPPING & ABDUCTION')
#     plt.plot(d1['Locality'], d1['ROBBERY'], label='ROBBERY')
#     plt.plot(d1['Locality'], d1['BURGLARY'], label='BURGLARY')
#     plt.plot(d1['Locality'], d1['THEFT'], label='THEFT')
#     plt.plot(d1['Locality'], d1['DOWRY DEATHS'], label='DOWRY DEATHS')
#
#     return d1