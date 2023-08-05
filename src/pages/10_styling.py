import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/styling',
    title='add style',
    name='add style',
    icon='fa-regular fa-gem'
    )

layout = html.Div(children=[
    html.H1(children='Add some style to your application.'),

    dcc.Markdown('''
    Most of us are researchers, not designers.
    But you do not want your users to exit your application because its cluttered, unreadable or hard-to-use. 
    However, good design is not easy and usually time-consuming.
    Time you might rather spent on your own research or explaining it to others. 
    Nevertheless a pretty application is important.
    Evidently i am no expert, but i will share some easy to implement strategies i use. 
    '''),

    html.H3(children='1). Add a theme'),

    dcc.Markdown('''
    Adding a theme is as simple as changing the application initialization.              
    '''),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
external_stylesheets = [
    dbc.themes.SIMPLEX,
    dbc.icons.BOOTSTRAP,
    dbc.icons.FONT_AWESOME
]

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)
      
        '''
    ),

    dcc.Markdown('''
    dash-bootstrap-components doesn't come with CSS included. 
    This is to give you the freedom to use any Bootstrap v5 stylesheet of your choice, so you can achieve the look you want in your app.     

    There are numerous free to use Bootstrap stylesheets available on the web.
    To start with, we recommend experimenting with some of the Bootswatch themes available in the dash_bootstrap_components.themes module.
    The full list of available themes is CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR.    
    
    Check out the [theme explorer](https://hellodash.pythonanywhere.com/) for a live demo of dash-bootstrap-components using all of the different available themes. 
    '''),

    html.H3(children='2). Standardization'),

    dcc.Markdown('''
    There is a reason you understand where clicking the following icons will bring you.              
    '''),

    html.I(className='fa-brands fa-github fa-2xl', style={'margin-left':'10px'}),
    html.I(className='fa-brands fa-youtube fa-2xl', style={'margin-left':'10px', 'color':'#ff0000'}),
    html.I(className='fa-brands fa-twitter fa-2xl', style={'margin-left':'10px', 'color':'#1DA1F2'}),

    html.Br(),

    dcc.Markdown('''
                 You can either work on creating your own great-design style.
                 But instead, consider copying successful style. A lot of websites follow specific formulas, because they works.
                 Do you need to implement a component users might be familiar with? 
                 Make sure the component follows standard design rules. 
                 For example, by including an arrow on the button you immediatly expect a dropdown menu. 
    '''),

    html.Div([
        dbc.DropdownMenu(
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Soups"),
                dbc.DropdownMenuItem("Burgers"),
                dbc.DropdownMenuItem("Icecreams"),
            ]
        ),

    html.Br(),
        dcc.Markdown('''
    vs.                 
    '''),

        dbc.Button('Menu', id='example-menu', n_clicks=0),
    ]),

    html.Div(id='menu_options'),

    html.Br(),

    html.H3(children='3). Favicon and Titles'),

    dcc.Markdown('''
    A favicon is a small icon or collection of icons associated with a website, web page, or web application. 
    It’s displayed within the browser tabs and bookmarks bar. 
    The examples below show the favicons for Google, Netflix, and CPCLab within the browser tab.
    Can you spot what could be done better?                  
                 
    In our case Dash handles the display of the favicon. Simply add a 'favicon.ico' file to your assets folder to start using it. 
    An ico file is a image file just like any .jpg or .png. Any modern image editing program can export to ico format. 
    Be wary that large icon files are not handled correctly in all (old) applications. 
'''),

    dbc.Row([
        dbc.Col([
            html.Img(src='assets/favicon_examples.png', alt='layout-figure', style={'display':'flex', 'width':'70%', 'margin':'auto', 'justify-content':'center', 'margin-top':'30px'}),            
        ]),
    ]),

    dcc.Markdown('''
    To title of our pages is handled by Dash as well. In our page setup we can change the title.
    '''),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        highlightLines = {
            4: {'color':'green'},
        },
        children='''
    dash.register_page(
    __name__,
    path='/styling',
    title='add style',
    name='add style',
    icon='fa-regular fa-gem'
    )'''),

    
], style={'margin-left':'10px'})

menu = [
    dbc.Button('Soups'),
    dbc.Button('Burgers'),
    dbc.Button('Icecreams'),
]

@callback(
    Output("menu_options", "children"),
    Input('example-menu', 'n_clicks')
)
def on_button_click(n):
    if n == 0:
        return
    elif (n % 2) == 0:
        return
    else:
        return menu