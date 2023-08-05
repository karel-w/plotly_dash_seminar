import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

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
    We might want to seperate data types, graph types or just plain information such as contact pages.
    We could make a long scrollable page (which is not necessarily bad), or we could add in pages to seperate our information.
    Here we will take a look how to host content in seperate pages.
    One style i'm particular fond of is a small advertisement bar in the top of the page, such as logos from your institution, funding agency, working group etc. 
    Then i add a simple navigation bar to the left to seperate my content and host the content in the middle as image belowed.
    '''),

    dbc.Row([
        dbc.Col([
            html.Img(src='assets/layout_example.png', alt='layout-figure', style={'display':'flex', 'width':'70%', 'margin':'auto', 'justify-content':'center', 'margin-top':'30px'}),            
        ]),
    ]),

    dcc.Markdown('''
    We have will create an app.layout hosting the sidebar, a row for our figures and a container to host our content.
    '''),

    html.H3(children=[
        'application.py'
    ]),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
                highlightLines = {
            1: {'color':'green'},
            4: {'color':'green'},
            5: {'color':'green'},
            13: {'color':'green'},
        },
        children='''
app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    sidebar,
    dbc.Row(
        [
            html.Img(src='assets/HDS_LEE_Logo_RGB_cut.png', alt='logo1', style={'width':'325px', 'height':'40px', 'margin-top':'10px'}),
            html.Img(src='assets/logo_cbc.png', alt='logo2', style={'width':'111px', 'height':'55px', 'margin-top':'2px'}),
            html.Img(src='assets/logo_cpc.png', alt='logo3', style={'width':'111px', 'height':'55px', 'margin-top':'2px'}),
            html.Img(src='assets/logo_jsc.png', alt='logo4', style={'width':'314px', 'height':'60px'}),
        ], style={'background-color':'#ADD8E6'}
    ),
    dash.page_container,
    ], style={'margin-left':'6rem'})     
    '''),

    dcc.Markdown('''
    The code for the sidebar                 
    '''),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        highlightLines = {
            15: {'color':'green'},
            17: {'color':'green'},
            22: {'color':'green'},
            29: {'color':'green'},
        },
        children='''
sidebar = html.Div(
        [
            html.Div(
                [
                    # width: 3rem ensures the logo is the exact width of the
                    # collapsed sidebar (accounting for padding)
                    html.Img(src='assets/HDS_LEE_Logo_RGB_small.png', style={"width": "3rem"}),
                    html.H2("Content"),
                ],
                className="sidebar-header",
            ),

            html.Hr(),

            dbc.Nav(
                [
                    dbc.NavLink(
                        [html.I(className=page['icon']), html.Span(f"{page['name']}", style={'margin-left':'8px'})],
                        href=page['path'],
                        active='exact',
                    )
                    for page in dash.page_registry.values()
                    
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="sidebar",
    )
'''
    ),

    html.H3(children=[
        'pages/01_example.py'
    ]),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        highlightLines = {
            4: {'color':'green'},
        },
        children='''
import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/empty',
    title='empty page',
    name='empty page',
    icon='fa-solid fa-file-circle-plus'
    )

layout = html.Div(children=[
    html.H1(children='This is a code example of a empty page.'),
    
], style={'margin-left':'10px'})

'''),
    

], style={'margin-left':'10px'})

