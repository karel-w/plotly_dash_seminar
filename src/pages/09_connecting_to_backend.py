import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/backend',
    title='connect ML code',
    name='connect ML code',
    icon='fa-solid fa-circle-nodes'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

