'''
1) Obtain the repo from git


2) Create a conda environment

conda create --name dash_tutorial
conda install -c conda-forge dash
conda install -c conda-forge dash-bootstrap-components
'''

import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/hello-world',
    title='hello-world',
    name='hello-world',
    icon='fa-solid fa-earth-europe'
    )

layout = html.Div(children=[
    html.H1(children='Hello World example'),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

data = pd.read_csv('../data/time_series.csv', index_col = 0)

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Hello world: Time series analysis'),
    dcc.Graph(id='time-series-graph'),
    dcc.RangeSlider(0, len(data), value=[0, len(data)], id='time-series-slider')
])


@callback(
    Output('time-series-graph', 'figure'),
    Input('time-series-slider', 'value')
)
def update_graph(value):
    print(value)
    df = data.iloc[value[0]:value[1]]

    fig = px.line(df)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
        '''
    ),
], style={'margin-left':'10px'})
