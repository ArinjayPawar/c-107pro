import pandas as pd
import csv
import plotly.graph_objects as pg
import numpy as np
import matplotlib.pyplot as mp
import plotly.express as px 


df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())


x=df.groupby("level")["attempt"].mean()
y=['Level1','Level2','Level3','Level4']
orientation='h',
colors=["red","green","blue","black"]
sizes=[200,200,200,200]
                     
mp.scatter(x,y,s=sizes, c=colors)
mp.colorbar()
mp.show()



student_df=df.loc[df['student_id']=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())

