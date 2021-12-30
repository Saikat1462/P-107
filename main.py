import pandas as pd
import csv
import plotly.graph_objects as go
import numpy as np
n=10000
df=pd.read_csv("data.csv")
student_df=df.loc[df["student_id"]=="TRL_mno"]
print(student_df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Scatter(
    x=student_df.groupby("level")["attempt"].mean(),
    y=["Level1","Level2","Level3","Level4"],
    orientation="h",        
    mode = 'markers',
    marker=dict(
        color=np.random.randn(n),
        colorscale='Thermal',
        showscale=True
    )
))
fig.show()