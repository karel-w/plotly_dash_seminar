import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/deployment-panyw',
    title='deployment',
    name='deployment',
    icon='fa-solid fa-python'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

