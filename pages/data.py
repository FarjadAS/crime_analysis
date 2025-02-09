import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/data', name="Data")

# LOAD DATASET
crime_df = pd.read_csv("crime.csv")

# PAGE LAYOUT
layout = html.Div(children=[
    html.Br(),
    html.Div(
        dash_table.DataTable(
            data=crime_df.to_dict('records'),
            page_size=20,
            style_cell={
                "background-color": "rgba(128, 128, 128, 0.2)",  # Slight shade of grey
                "border": "solid 1px white",
                "color": "black",
                "font-size": "11px",
                "text-align": "left",
            },
            style_header={
                "background-color": "black",  # Dark header color
                "font-weight": "bold",
                "color": "white",
                "padding": "10px",
                "font-size": "18px",
            },
        ),
        style={'width': '100%', 'overflowX': 'auto'}
    ),
])
