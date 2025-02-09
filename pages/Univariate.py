import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output


crime_df = pd.read_csv("crime.csv")

dash.register_page(__name__, path='/univariate', name="Uni-Variate")


columns = ["Vict Age", "Part 1-2", "Hour" , "Crm Cd","Status Desc", "LOCATION", "Crm Cd Desc","Area Name","Vict Sex"]


layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dcc.Dropdown(id="dist_column", options=[{'label': col, 'value': col} for col in columns], value="Vict Age", clearable=False),
    dcc.Graph(id="histogram"),
    html.H2('box plot'),
    dcc.Dropdown(id="box_column", options=[{'label': col, 'value': col} for col in columns], value="Vict Age", clearable=False),
    dcc.Graph(id="box"),
])

@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)

def create_distribution(col_name="Vict Age"):
    return px.histogram(data_frame=crime_df, x=col_name, height=600)

@callback(Output("box", "figure"), [Input("box_column", "value"), ])
def update_histogram(box_column):
    return create_box(box_column)

def create_box(col_name="Vict Age"):
    return px.box(data_frame=crime_df, x=col_name, height=600)