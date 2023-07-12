import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/deployment-easy',
    title='deployment: easy',
    name='deployment: easy',
    icon='fa-solid fa-python'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

