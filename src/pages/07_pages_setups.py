import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/pages',
    title='multi-page',
    name='multi-page',
    icon='fa-solid fa-file-lines'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

