import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

dash.register_page(
    __name__,
    path='/links',
    title='helpful links',
    name='helpful links',
    icon='fa-solid fa-link'
    )

card1 = dbc.CardGroup(
    [
        dbc.Row([
            #Card 1
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='https://img.freepik.com/premium-vector/red-youtube-logo-social-media-logo_197792-1803.jpg?w=2000',
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start',
                            ),
                        ], 
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('@Charming Data', className='card-title'),
                                    dcc.Markdown('''
                                    Charming Data is a youtube channel run by the community manager of dash.
                                    He created over 100 videos on plotly graphs, dash components, connecting components, bootstrap, deployment, full dashboards, etc.
                                    If you want inspiration or just want to figure out a specific components, his tutorials are a great start.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        '@Charming Data', color='info', className='mt-auto', href='https://www.youtube.com/@CharmingData', outline=True
                                    ),
                                ]
                            ),
                            ], className='g-0 col-md-9', style={'text-align':'justify'}
                        ),

                    ]
                )
            ], className='w-75'),
           
        ]),
    ]
)

card2 = dbc.CardGroup(
    [
        dbc.Row([
            #Card 1
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='https://static.thenounproject.com/png/399116-200.png',
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start',
                            ),
                        ], 
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('Cheatsheets', className='card-title'),
                                    dcc.Markdown('''
                                    There is no need to reinvent the wheel. Sometimes a good base can bring you quite a ways. 
                                    The cheatsheets are constructed as interactive dashboards. This can also give you some ideas how to style your own.
                                                 
                                    **Bootstrap CSS** explores how you can use CSS to style each dash-bootstrap-component. 
                                                
                                    In the **Themes explorer** you can view different themes with various charts.
                                                 
                                    **Example figures** is a collection of plug-and-play plotly figures together with simple data selection components. 
                                    ''',
                                    className='card-text',
                                    ),
                                    html.Div([
                                        dbc.Button(
                                            'Bootstrap CSS', color='info', className='me-1', href='https://dashcheatsheet.pythonanywhere.com/', outline=True
                                        ),
                                        dbc.Button(
                                            'Themes explorer', color='info', className='me-1', href='https://hellodash.pythonanywhere.com/', outline=True
                                        ),
                                        dbc.Button(
                                            'Example figures', color='info', className='me-1', href='https://www.youtube.com/@CharmingData', outline=True
                                        ),
                                    ]),
                                ]
                            ),
                            ], className='g-0 col-md-9', style={'text-align':'justify'}
                        ),

                    ]
                )
            ], className='w-75'),
           
        ]),
    ]
)

layout = html.Div(children=[
    html.H1(children='Helpful links.'),

    card1,

    html.Br(),

    card2,

], style={'margin-left':'10px'})

