import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/styling',
    title='add style',
    name='add style',
    icon='fa-regular fa-gem'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

