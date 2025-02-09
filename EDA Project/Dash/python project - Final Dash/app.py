from dash import Dash, html, dcc
import dash
import plotly.express as px
import dash_bootstrap_components as dbc

px.defaults.template = "ggplot2"

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=[dbc.themes.LUX] + external_css)
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row([
		dbc.Col(html.Img(src="assets/CrimeLab.jpeg", style={'width': '130px', 'height': '100px'}), width=1),
        dbc.Col(html.Div("Crime Data Analysis",
                         style={'fontSize':50, 'textAlign':'center','color': 'white'}))
    ],
	style={'backgroundColor': 'black'},),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == '__main__':
	app.run(debug=True)