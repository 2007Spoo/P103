import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="\tcountry", y="date",size="cases",color="Country",size_max=100)
fig.show()

