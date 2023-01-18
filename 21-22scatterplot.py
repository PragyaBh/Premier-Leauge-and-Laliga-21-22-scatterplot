#importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


#importting csv file
df=pd.read_csv('path\\filename.csv')


#data preview
df.head()


#removing rows with missing value
df=df.dropna()


#selecting column for scatter plot
df=df[['Squad','npxG_p90','npxG_pSh']]

#data preview
df.head()


#converting columns into list
lists={}
for column in df.columns:
    lists[column]=df[column].tolist()

print(lists)


#creating scatter plot
fig = px.scatter(df,x='npxG_pSh', y='npxG_p90', text='Squad',title='EPL and Laliga: Chances Creation')


#asigning colors to grid lines
fig.layout.xaxis.gridcolor="white"
fig.layout.yaxis.gridcolor="white"


#customizing scatter plot

fig.update_layout(uniformtext_minsize=16, uniformtext_mode='hide',font_family='Arial', plot_bgcolor="bisque", 
                  autosize=False, width=1000, height=850,titlefont=dict(family='Arial',size=26),
                   paper_bgcolor="bisque",font = dict(color='black'), 
                  xaxis=dict(title_text="npxG per Shot",titlefont=dict(family='Arial',size=24)), 
                  yaxis=dict(title_text="npxG created per 90", titlefont=dict(family='Arial',size=24)));


#alternating text position
fig.data[0].textposition=['bottom right' if i%2==0 else 'top left' for i in range(len(df))]


#assigning color
fig.data[0].marker.color=['red' if i <20 else 'rebeccapurple' for i in range(len(df))]


#adding annotation to the chart

fig.update_layout(annotations=[dict(x=1, y=1.06, xref='paper', yref='paper',
             text='Premier Leauge', showarrow=False, font=dict(family='Arial',color='red',size=18)),
        dict(x=0.906, y=1.03, xref='paper', yref='paper',
             text='Laliga', showarrow=False, font=dict(family='Arial',color='rebeccapurple',size=18)),
dict(font=dict(color='black',size=12),x=0.85, y=-0.11,showarrow=False,text="pragya.bh | data via FBref",textangle=0,
     xanchor='left',xref="paper",yref="paper")]);


#displaying 
fig.show()