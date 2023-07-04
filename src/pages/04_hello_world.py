'''
1) Obtain the repo from git


2) Create a conda environment

conda create --name dash_tutorial
conda install -c conda-forge dash
conda install -c conda-forge dash-bootstrap-components
'''

import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/hello-world',
    title='hello-world',
    name='hello-world',
    icon='fa-solid fa-earth-europe'
    )

data = pd.read_csv('../data/time_series.csv', index_col = 0)

layout = html.Div(children=[
    html.H3(children='Why Dash?'),

    html.Div(children='''
    Dash is a framework for building data apps in Python. You can use it to create point-&-click interfaces to models written in Python.
    Dash has a open source framework for developing data apps in pure Python, without having to learn JavaScript, CSS or HTML. 

    Dash also operates in the enterpise market. Here it focusses on offering low-code development tools, deployment & scaling tools and IT integration for enterprises.
    '''),

    html.Br(),

    html.Div(children='''
    For the scientific community the open source version is often good enough, as you can still do everything through python.
    The major drawback of the open source version is the lack of support for deploying your app to the public. 
    But in this course i'll show you how to deploy your app using the eu.pythonanywhere.com and how to deploy your app on a apache webserver.

    '''), 

    html.Br(),

    html.H3(children='My first dash app'),

    html.Div(children='''
    Dash apps are really easy to build, here we'll walk through a simple app that displays a time series for which you can edit your timeline.
    The data displayed here are values switching between +1 and -1 values. When you look at the full range of the data you can hardly see the pattern.
    But when you change the slider below to different timescales you can see the pattern and flips between values more clearly.
    '''), 

    html.Br(),

    dcc.RangeSlider(0, len(data), value=[0, len(data)], id='time-series-slider'),

    dcc.Graph(id='time-series-graph'),

    html.Br(),

    html.Div(children='''
    So how do we do this?
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd        
        '''
    ),

    html.Div(children='''
    Just as regular we import the libraries we need. We import Dash for setting up the server.
    Instead of using html we can import the dash html wrappers. Which essentially turn html into python.
    dcc is imported for the dash-core-components. Later on we'll see dbc and dmc, dash-bootstrap-components and dash-mantine-components.
    Input, Output and callback are used for writing python functions which update what you want to display on the dash app.
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
data = pd.read_csv('../data/time_series.csv', index_col = 0)
'''),

    html.Div(children='''
    Lets load in some data using pandas. There are different ways to handle data loading. You can load data from the server.
    However you can also load in data from online sources. There are even options to load in data from the client side and handle processing and calculations on the client side.
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
app = Dash(__name__)
        '''
    ),

    html.Div(children='''
    We start a flask server using Dash. This server is essentially the backbone running the code.
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
app.layout = html.Div([
    html.H1('Hello world: Time series analysis'),
    dcc.Graph(id='time-series-graph'),
    dcc.RangeSlider(0, len(data), value=[0, len(data)], id='time-series-slider')
])        
        '''
    ),

    html.Div(children='''
    app.layout describes how our page will look. We can use text components, graph components, buttons, sliders, etc. 
    To see all available components you can check the documentation for dash core components (https://dash.plotly.com/dash-core-components), dash bootstrap components (https://dash-bootstrap-components.opensource.faculty.ai/), dash mantime components (https://www.dash-mantine-components.com/) 
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
@callback(
    Output('time-series-graph', 'figure'),
    Input('time-series-slider', 'value')
)
def update_graph(value):
    df = data.iloc[value[0]:value[1]]

    fig = px.line(df)

    return fig        
        '''
    ),

    html.Div(children='''
    Here we see an example of a callback function. Using the callback decorator from dash we can give an output and input to this function.
    Here the output is a figure with id: 'time-series-graph'. The input is a value which we obtain from the component with id 'time-series-slider'.
    The function itself makes a copy of the data frame between particular values from the slider. Then using plotly we create a simple plot and return this figure.
    '''),

    html.Br(),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')     
        '''
    ),

    html.Div(children='''
    Finally we need to run the server when we execute the python file. Here we run it locally on our machine. 
    Later on we'll see how to change this to serve the dashboard to other users. 
    '''),

    html.Br(),
    html.Br()

], style={'margin-left':'10px'})

@callback(
    Output('time-series-graph', 'figure'),
    Input('time-series-slider', 'value')
)
def update_graph(value):
    df = data.iloc[value[0]:value[1]]

    fig = px.line(df)

    return fig