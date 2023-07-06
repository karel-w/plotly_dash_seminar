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
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start',
                            ),
                        ], 
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('ProteInfer', className='card-title'),
                                    dcc.Markdown('''
                                    I want to introduce you to ProteInfer, an interactive paper presenting a convolutional neural network tool for predicting enzymatic function from amino acid sequences.
                                    It offers a unique learning experience by allowing you to test the tool as you read the paper.
                                    The interactive figures in the machine learning model section provide additional insights into how the model operates when you hover over them.
                                    ProteInfer also includes interactive graphs, like Figures 8 and 9, enabling exploration of the embedding space in machine learning and enhancing understanding of the discovered patterns and relationships.
                                    This interactive approach transforms the traditional paper reading experience into an engaging and interactive process.
                                    I encourage you to dive into the paper, interact with its features, and discover the potential of ProteInfer in predicting enzymatic function.
                                    Interactive papers like ProteInfer pave the way for innovative research presentation methods and foster a collaborative learning environment.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'ProteInfer', color='info', className='mt-auto', href='https://google-research.github.io/proteinfer/', outline=True
                                    ),
                                ]
                            ),
                            ], className='g-0 col-md-9', style={'text-align':'justify'}
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
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start',
                            ),
                        ],
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('A Gentle Introduction to Graph Neural Networks', className='card-title'),
                                    dcc.Markdown('''
                                    Here I want to discuss an exceptional interactive paper. 
                                    Within this article, you will find interactive plots showcasing graphs and Graph Neural Networks (GNNs), allowing you to hover over nodes, edges, and information to observe the intricate connections between them. 
                                    Through this interactive exploration, you will gain insights into the conversion of images or text into graphs, unraveling the underlying mechanisms of this transformation process.
                                    The tools presented in this paper allows you to delve into the interconnectedness of information within graphs and observe how information propagates through them.
                                    By immersing yourself in the interactive plots, you can visually dissect the propagation patterns and comprehend the intricate dynamics within graph-based representations.
                                    This interactive paper not only provides a comprehensive understanding of graph analysis but also serves as a stepping stone for exploring the broader potential of graph-based methodologies.
                                    It is a remarkable demonstration of the power of interactive visualization and its role in advancing our understanding of complex systems.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'GNN Introduction', color='info', className='mt-auto', href='https://distill.pub/2021/gnn-intro/', outline=True
                                    ),
                                ]
                            ),
                            ], 
                            className='g-0 col-md-9', style={'text-align':'justify'}
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
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ],
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('TopEnzyme', className='card-title'),
                                    dcc.Markdown('''
                                    Here I present a tool that I personally developed called TopEnzyme.
                                    The primary objective behind its creation was to construct an enzyme database for a machine learning project.
                                    With the recent release of AlphaFold2, our goal was to evaluate its performance and assess the extent of coverage it provides within the enzyme space.
                                    Initially, our plan was solely to release the database; however, we realized that this alone would not be sufficient for life scientists who require guidance on working with databases.
                                    To address this, we developed a browseable map, which enables users to explore the known (structural) enzyme space. We incorporated features like filters, scores, and information cards to enhance usability and provide comprehensive information to the users.
                                    An important lesson we learned from this endeavor is the significant impact of interactive tools in impressing reviewers and enhancing the overall research presentation.
                                    Interactive tools not only facilitate data exploration but also serve as effective means of communication, leaving a lasting impression on reviewers and readers alike.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'TopEnzyme', color='info', className='mt-auto', href='https://cpclab.uni-duesseldorf.de/topenzyme/', outline=True
                                    ),
                                ]
                            ),
                            ], className='g-0 col-md-9', style={'text-align':'justify'}
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
                            src='assets/baustatik_example.png',
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ],
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('Baustatik', className='card-title'),
                                    dcc.Markdown('''
                                    I want to highlight an educational tool called Baustatik, which leverages interactive graphs to enhance the teaching experience.
                                    You may recall force diagrams (free body diagrams) from your high school physics classes.
                                    Now, imagine being able to modify the forces and observe the immediate impact on the system, all within your web browser.
                                    Baustatik allows you to explore various aspects of modeling buildings by manipulating forces, positions, and objects, enabling you to witness firsthand how specific properties respond to these changes.
                                    This interactive app provides a unique opportunity to develop a deeper intuition about the concepts you are modeling with mathematical formulas. 
                                    By interacting with the graphs, you gain a tangible understanding of the cause-and-effect relationships within structural systems.
                                    Baustatik bridges the gap between theory and practical application, fostering a more comprehensive and intuitive grasp of the subject matter. 
                                    It is an outstanding example of how technology can revolutionize the learning experience, making complex concepts more accessible and engaging.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'Baustatik', color='info', className='mt-auto', href='https://baustatik.herokuapp.com/', outline=True
                                    ),
                                ]
                            ),
                            ], className='g-0 col-md-9', style={'text-align':'justify'}
                        ),

                    ]
                )
            ], className='w-75'),

            #card 5
            dbc.Card([
                dbc.Row(
                    [
                        dbc.Col([
                            dbc.CardImg(
                            src='assets/dash_gallery_example.png',
                            style={'margin':'auto', 'justify-content':'center'},
                            className='img-fluid rounded-start align-items-center',
                            ),
                        ],
                        style={'display':'flex', 'justify-content':'center', 'align-items':'center'},
                        className='col-md-3'),

                        dbc.Col([
                            dbc.CardBody(
                                [
                                    html.H5('Dash Gallery', className='card-title'),
                                    dcc.Markdown('''
                                    While my expertise may not lie in the fields of energy and earth, I can still appreciate the value of interactive graphs within these domains. 
                                    From exploring the Dash gallery, we can observe numerous examples of how interactive graphs can effectively communicate complex information and convey a comprehensive story. 
                                    One notable example is a now-inactive app called [datashader_powergrid](https://github.com/databyjp/datashader_powergrid), which visualized the solar and wind capacity across the United States. 
                                    This app allowed users to select custom resolutions, enabling them to explore solar and wind capacity at various levels of detail. Such interactive tools have immense potential in the energy and earth research fields. 
                                    They can be utilized to analyze and visualize renewable energy potential, map resource distribution, study climate change patterns, and assess the environmental impact of energy production. 
                                    By empowering researchers to interact with the data, these interactive graphs provide a more engaging and intuitive way to comprehend complex energy and earth systems. 
                                    The ability to customize resolutions, explore geospatial data, and manipulate variables fosters a deeper understanding of the factors influencing energy generation and resource availability. 
                                    In the context of energy and earth research, interactive graphs serve as powerful tools for data exploration, hypothesis generation, and effective communication of research findings. 
                                    While the specific app mentioned may no longer be active, its concept exemplifies the potential impact of interactive graphs in the analysis and understanding of energy and earth-related data.
                                    ''',
                                    className='card-text',
                                    ),
                                    dbc.Button(
                                        'Dash gallery', color='info', className='mt-auto', href='https://dash.gallery/Portal/', outline=True
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


layout = html.Div(children=[
    html.H1(children='Why do we want to use interactive graphs?'),

    dcc.Markdown('''
    Lets explore some implementations of interactive graphs and papers and discuss these in class.    
    '''),
    
    cards
], style={'margin-left':'10px', 'margin-right':'20px'})

