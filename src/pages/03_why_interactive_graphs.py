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
    path='/why',
    title='why?',
    name='why?',
    icon='fa-solid fa-question'
    )

layout = html.Div(children=[
    html.H1(children='Why?'),
    
], style={'margin-left':'10px'})

