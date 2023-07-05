import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/path',
    title='empty page',
    name='empty page',
    icon='fa-solid fa-file-circle-plus'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

