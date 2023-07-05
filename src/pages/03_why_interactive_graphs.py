import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/why',
    title='why?',
    name='why?',
    icon='fa-solid fa-question'
    )

cards = dbc.CardGroup(
    [
        dbc.Row([
            #Card 1
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='assets/ProteInfer_example.png',
                            style={'margin-top':'22px'},
                            className='img-fluid rounded-start',
                            ),
                        ], className='col-md-2'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('ProteInfer', className='card-title'),
                                    dcc.Markdown('''
                                    ProteInfer is a convolutional neural network tool to predict enzymatic function from a amino acid sequence. 
                                    What is interesting that its presented as an interactive paper. 
                                    You can immediatly test the tool they developed in the context of the paper.
                                    While reading the section on the machine learning model you can hover over the added figure to get a better understanding of how the model operates.
                                    Interactive graphs are also really interesting for exploring embedding space in machine learning. Figure 8 and 9 in the paper are great examples of this.

                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'ProteInfer', color='success', className='mt-auto', href='https://google-research.github.io/proteinfer/'
                                    ),
                                ]
                            ),
                            ], className='col-md-10',
                        ),

                    ]
                )
            ], className='w-75'),
            #Card 2
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='assets/GNN_introduction_example.png',
                            style={'margin-top':'50px'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ], className='col-md-2'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('A Gentle Introduction to Graph Neural Networks', className='card-title'),
                                    dcc.Markdown('''
                                    This article is a great example of an interactive paper. 
                                    Here graphs and GNNs are presented in interactive plots, where you can hover over nodes, edges, information to see how its all connected.
                                    You explore how images or text can be converted to graphs.
                                    The tools in this paper really allow you to look at how information is connected in graphs and how information is propegated through graphs.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'GNN Introduction', color='success', className='mt-auto', href='https://distill.pub/2021/gnn-intro/'
                                    ),
                                ]
                            ),
                            ], className='col-md-8',
                        ),

                    ]
                )
            ], className='w-75'),

            #card 3
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='assets/TopEnzyme_no_bg.png',
                            style={'margin-top':'50px'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ], className='col-md-2'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('TopEnzyme', className='card-title'),
                                    dcc.Markdown('''
                                    TopEnzyme is a tool i build myself. 
                                    My goal was to create an enzyme databases for a machine learning project.
                                    AlphaFold2 was just released and we needed to figure out how good it was. 
                                    Besides comparing quality we also wanted to see how much of the enzyme space is now covered.
                                    First we thought of only releasing the database, but this is not much help to general life scientist, as they need to know how to work with databases.
                                    So we made a browseable map, where users can browse known (structural) enzyme space. We added things like filters, scores and information cards.
                                    One important thing we learned from this is that interactive tools are really good for impressing reviewers.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'TopEnzyme', color='success', className='mt-auto', href='https://cpclab.uni-duesseldorf.de/topenzyme/'
                                    ),
                                ]
                            ),
                            ], className='col-md-8',
                        ),

                    ]
                )
            ], className='w-75'),

            #card 4
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='assets/dash_gallery_example.png',
                            style={'margin-top':'50px'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ], className='col-md-2'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('Dash Gallery', className='card-title'),
                                    dcc.Markdown('''
                                    Unfortunately i'm not at home in the fields of energy and earth. 
                                    However from looking through the dash gallery we can see many examples of incorperating maps to tell the full story.
                                    Unfortunately [this](https://github.com/databyjp/datashader_powergrid) app is not live anymore.
                                    But it showed the solar/wind capacity in the US, where you can select at custom resolutions to find out the solar and wind capacity.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'Dash gallery', color='success', className='mt-auto', href='https://dash.gallery/Portal/'
                                    ),
                                ]
                            ),
                            ], className='col-md-8',
                        ),

                    ]
                )
            ], className='w-75'),


           
        ]),
    ]
)


layout = html.Div(children=[
    html.H1(children='Why do we want to use interactive graphs?'),

    dcc.Markdown('''
    Lets explore some implementations of interactive graphs and papers and discuss these in class.    
    '''),
    
    cards
], style={'margin-left':'10px', 'margin-right':'20px'})

