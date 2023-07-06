import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/callbacks',
    title='callbacks',
    name='callbacks',
    icon='fa-solid fa-at'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

