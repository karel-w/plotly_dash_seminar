import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc

dash.register_page(
    __name__,
    path='/pages',
    title='multi-page',
    name='multi-page',
    icon='fa-solid fa-file-lines'
    )



layout = html.Div(children=[
    html.H1(children='Creating a multi-page application'),

    dcc.Markdown('''
    Sometimes we want to seperate data or information into different sections.
    We could make a long scrollable page, or we could add in a navigation bar to go to different pages.
    '''),

    
], style={'margin-left':'10px'})

