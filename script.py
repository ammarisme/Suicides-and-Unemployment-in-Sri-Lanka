# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:10:53 2019

@author: ammar
"""

import pandas as pd 
import matplotlib.pyplot as plt
"""
nature_of_occupation = pd.read_csv("./datasets/nature_of_occupation.csv") 

def get_data_for_year(year, year_data):
    year_data = year_data.loc[:, year_data.columns.str.startswith((year,"Age"))]
    year_data.loc[:, year_data.columns != 'Age group']= year_data.loc[:, year_data.columns != 'Age group'].apply(pd.to_numeric)
    return year_data;

nature_2014 = get_data_for_year("2014", nature_of_occupation)
nature_2015 = get_data_for_year("2015", nature_of_occupation)
nature_2016 = get_data_for_year("2016", nature_of_occupation)
nature_2017 = get_data_for_year("2017", nature_of_occupation)


def get_total_unemployed(dataset, year):
    total_unemployed = dataset.loc[:,dataset.columns.str.find("Unemployed" ) > 0 ]
    return total_unemployed[year+'_Unemployed persons_M'][0:10].sum()+total_unemployed[year+'_Unemployed persons_F'][0:10].sum()

def get_normal_suicides(dataset):
    all_suicides = dataset.loc[:,dataset.columns.str.find("Age group" ) < 0 ]
    total = 0
    for key in all_suicides.keys():
        total = total + all_suicides[key][1:10].sum()
    return total
        
    return total_unemployed[year+'_Unemployed persons_M'][1:10].sum()+total_unemployed[year+'_Unemployed persons_F'][1:10].sum()
    
presentation_data = pd.DataFrame({
        'unemployed_suicides' : [
                get_total_unemployed(nature_2014 , "2014"),
                get_total_unemployed(nature_2015 , "2015"),
                get_total_unemployed(nature_2016 , "2016"),
                get_total_unemployed(nature_2017 , "2017")], 
        "unemployment_rates" : [4.3 , 4.7 , 4.4 ,  4.2] , 
        "normal_suicides" : [ 
                get_normal_suicides(nature_2014),
                get_normal_suicides(nature_2015), 
                get_normal_suicides(nature_2016),
                get_normal_suicides(nature_2017) ]
        } , index = ["2014" , "2015" , "2016" , "2017"])

presentation_data['unemployed_suicide_rate'] = presentation_data['unemployed_suicides'] / presentation_data['unemployment_rates']   
presentation_data['employed_suicide_rate'] = presentation_data['normal_suicides'] / (100 - presentation_data['unemployment_rates'])
"""
from matplotlib.pyplot import *
"""
fig, ax = subplots()
df = presentation_data[['unemployed_suicide_rate','employed_suicide_rate']]
df.plot(kind='bar', ax=ax)
ax.legend(["Suicide rates of unemployed", "Suicide rates of employed"]);

"""
fig, ax = subplots()
unemployed_suicides = presentation_data['unemployed_suicides']
unemployed_suicides.plot(kind='bar', ax=ax)
ax.legend(["Suicide of unemployed"]);



"""
df = pd.DataFrame({
...    'pig': [20, 18, 489, 675, 1776],
...    'horse': [4, 25, 281, 600, 1900]
...    }, index=[1990, 1997, 2003, 2009, 2014])
>>> lines = df.plot.line()
# Preview the first 5 lines of the loaded data 

fourteen = data.loc[:, data.columns.str.startswith('2014')]
fifteen = data.loc[:, data.columns.str.startswith('2015')]
sixteen = data.loc[:, data.columns.str.startswith('2016')]


seventeen = data.loc[:, data.columns.str.startswith(("2017","Age"))]
seventeen.loc[:, seventeen.columns != 'Age group']= seventeen.loc[:, seventeen .columns != 'Age group'].apply(pd.to_numeric)
seventeen['8_pass'] = seventeen['2017_School not attended_M']+ seventeen['2017_School not attended_F'] + seventeen['2017_From Grade 1 to 7_M'] +seventeen['2017_From Grade 1 to 7_F'] + seventeen['2017_Passed Grade 8_M'] +seventeen['2017_Passed Grade 8_F']
seventeen['Passed_school'] = seventeen['2017_Passed G.C.E (O/L)_M']+ seventeen['2017_Passed G.C.E (O/L)_F'] + seventeen['2017_Passed G.C.E (A/L)_M'] +seventeen['2017_Passed G.C.E (A/L)_F'] 
seventeen['Graduate'] = seventeen['2017_University Degree or above_M'] +seventeen['2017_University Degree or above_F']
seventeen['Total'] = seventeen['8_pass']  + seventeen['Passed_school']  +seventeen['Graduate'] 


seventeen.plot(kind='bar',x='Age group',y=['8_pass' ,'Passed_school','Graduate' ])
"""
#print(seventeen['8_pass'])


#fifteen = [col for col in data if col.startswith('2015')]
#fifteen.loc[:, data.columns != 'Age group']= fifteen.loc[:, fifteen.columns != 'Age group'].apply(pd.to_numeric)

#data.plot(x ='Age group', y='2017_Passed Grade 8_M', kind = 'bar')	
