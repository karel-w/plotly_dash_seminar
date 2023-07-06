import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/links',
    title='helpful links',
    name='helpful links',
    icon='fa-solid fa-link'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

