'''
1) Obtain the repo from git


2) Create a conda environment

conda create --name dash_tutorial
conda install -c conda-forge dash
conda install -c conda-forge dash-bootstrap-components
'''

import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/setup',
    title='setup',
    name='setup',
    icon='fa-solid fa-wrench'
    )

layout = html.Div(children=[
    html.H1(children='Setup'),
    
], style={'margin-left':'10px'})

