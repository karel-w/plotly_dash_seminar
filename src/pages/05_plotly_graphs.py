import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/plotly',
    title='plotly graphs',
    name='plotly graphs',
    icon='fa-solid fa-chart-line'
    )

layout = html.Div(children=[
    html.H1(children='enter your page here.'),
    
], style={'margin-left':'10px'})

