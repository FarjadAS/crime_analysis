import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Assuming 'crime.csv' contains your dataset
crime_df = pd.read_csv("crime.csv")

dash.register_page(__name__, path='/bivariate', name="Bi-Variate")

columns = ["Vict Age", "Part 1-2", "Hour" , "Crm Cd","Status Desc", "LOCATION", "Crm Cd Desc","Area Name","Vict Sex"]

layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dcc.Dropdown(id="x-column", options=[{'label': col, 'value': col} for col in columns], value="Vict Age", clearable=False),
    dcc.Dropdown(id="y-column", options=[{'label': col, 'value': col} for col in columns], value="Vict Age", clearable=False),
    dcc.Graph(id="bi-histogram")])

@callback(Output("bi-histogram", "figure"), [Input("x-column", "value"),Input("y-column", "value") ])
def update_histogram(x,y):
    return create_distribution(x,y)

def create_distribution(x="Vict Age",y="Part 1-2"):
    return px.histogram(data_frame=crime_df, x=x,color=y,barmode="group", height=600)