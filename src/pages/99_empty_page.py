import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc

dash.register_page(
    __name__,
    path='/empty',
    title='empty page',
    name='empty page',
    icon='fa-solid fa-file-circle-plus'
    )

layout = html.Div(children=[
    html.H1(children='This is a code example of a empty page.'),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/empty',
    title='empty page',
    name='empty page',
    icon='fa-solid fa-file-circle-plus'
    )

layout = html.Div(children=[
    html.H1(children='This is a code example of a empty page.'),
    
], style={'margin-left':'10px'})

'''),
    
], style={'margin-left':'10px'})

