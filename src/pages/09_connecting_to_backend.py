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
    html.H1(children='Under construction.'),

    html.Img(src='https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Bob_the_builder.jpg/220px-Bob_the_builder.jpg', alt='bob', style={'width':'314px'}),
    
], style={'margin-left':'10px'})

