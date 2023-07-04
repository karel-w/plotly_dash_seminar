import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/',
    title='home',
    name='home',
    icon='fa-solid fa-house'
    )
layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),

], style={'margin-left':'10px'})