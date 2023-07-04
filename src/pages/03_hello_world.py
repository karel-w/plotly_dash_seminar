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

        '''
    ),
], style={'margin-left':'10px'})
