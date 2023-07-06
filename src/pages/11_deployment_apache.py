import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/deployment-apache',
    title='deployment: apache',
    name='deployment: apache',
    icon='fa-solid fa-helicopter'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

