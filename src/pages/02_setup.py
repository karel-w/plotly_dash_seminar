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

dash.register_page(
    __name__,
    path='/setup',
    title='setup',
    name='setup',
    icon='fa-solid fa-wrench'
    )

layout = html.Div(children=[
    html.H1(children='Setup'),

    html.Br(),

    html.H3(children='1. Clone the git repository.'),

    dcc.Markdown(''' 
Make sure  you have git installed on your machine. Lets start by cloning the repository.

1. Open a terminal or command prompt on your local machine.
2. Change to the directory where you want to store the repository (if necessary).
3. Run the following command to clone the repository:
'''), 

    dmc.Prism(
        language='bash',
        withLineNumbers=False,
        children='''
git clone git@github.com:karel-w/plotly_dash_seminar.git
        '''
    ),

    html.H3(children='2. Setup your environment using Miniconda.'),

    dcc.Markdown(''' 
    Obtain miniconda from [here](https://docs.conda.io/en/latest/miniconda.html#installing).
    Follow miniconda installation instructions from [here](https://conda.io/projects/conda/en/stable/user-guide/install/index.html).

    Lets create a conda environment and install the required packages.
    '''),

    dmc.Prism(
        language='bash',
        withLineNumbers=False,
        children='''
conda env create --file environment.yml
conda activate dash_tutorial
        '''
    ),

    html.H3(children='3. Generate the mock data.'),

    dcc.Markdown(''' 
    Change to the data director and run generate_data.py with python.
    '''),

    dmc.Prism(
        language='bash',
        withLineNumbers=False,
        children='''
cd data/
python generate_data.py
        '''
    ),

    html.H3(children='4. Test the dashboard.'),

    dcc.Markdown(''' 
    Change back to the source directory and run the application.py file.
    '''),

    dmc.Prism(
        language='bash',
        withLineNumbers=False,
        children='''
cd ../src/
python application.py
        '''
    ),

    dcc.Markdown('''
    The application should automatically in your browser. If the browser doesn't open the page, navigate to [localhost:8050](localhost:8050)
    '''),


], style={'margin-left':'10px'})

