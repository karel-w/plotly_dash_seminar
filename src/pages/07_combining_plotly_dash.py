import dash
from dash import html, dcc, callback, Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from graphs.topenzyme_graph import topenzyme_graph_advanced

dash.register_page(
    __name__,
    path='/dash-plotly',
    title='combining dash + plotly',
    name='combining dash + plotly',
    icon='fa-regular fa-object-group'
    )

#Load in required data
data = pd.read_csv('../data/topenzyme_data.csv')
class_dictionary_df = pd.read_csv('../data/ec_dictionary_small.csv')
class_dictionary_df['class'] = class_dictionary_df['class'].str.strip()

##### SEARCH BAR ###############################################################################
#create the correct dictionary to search over from the data
data_part1 = class_dictionary_df[class_dictionary_df['class'].str.count('.') <= 6]
data_part2 = class_dictionary_df[class_dictionary_df['class'].isin(data['EC'])]

#match sub-classes present
subecs = data_part1['class'].tolist()
ecs = data['EC'].tolist()
matches = [y for x in ecs for y in subecs if y in x]
data_part1 = data_part1[data_part1['class'].isin(matches)]

#merge classes and subclasses
merged_data = pd.concat([data_part1, data_part2])

dict_list = []
for name, ec in zip(merged_data['names'].tolist(), merged_data['class'].tolist()):
    dict_list.append({'label': name, 'value': ec})

# class_dictionary = pd.concat([part1, part2]).set_index('class').to_dict()['names']
# print(merged_data)
# data_dict_list = []
# for ec in data['EC'].tolist():
#     data_dict_list.append({'label': ec, 'value': ec})

@callback(
    Output('dynamic_search', 'options'),
    Input('dynamic_search', 'search_value'),
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in dict_list if search_value.casefold() in o['label'].casefold()]
#################################################################################################
##### TopEnzyme Figure ##########################################################################
@callback(
    Output('topenzyme_figure', 'figure'),
    Input('dynamic_search', 'value'),
    Input('radioitems-inline-input', 'value'),
)
def update_figure(search_value, data_property):
    if search_value:
        if search_value.count('.') < 3:
            df = data[data['EC'].str.startswith(search_value + '.')]
        else:
            df = data[data['EC'].str.startswith(search_value)]
        
        fig = topenzyme_graph_advanced(df, cproperty=data_property)
    else:
        df = data
        fig = topenzyme_graph_advanced(df, cproperty=data_property)

    return fig
#################################################################################################
##### Residue Length Card setings ###############################################################



layout = html.Div(children=[
    html.H1(children='Combining dash and plotly.'),

    dcc.Markdown('''
    Now lets take a look at combining dash and plotly to see what we can do to create truly interactive and explorable figures.
    For this we'll take the TopEnzyme figure and significantly improve it. The code for each section is explained at the bottom of the page.
    '''),

    dbc.Row([
        dbc.Col([
            html.Br(),

            html.Br(),

            html.H4('Lets add a search bar:'),

            dcc.Dropdown(
            id = 'dynamic_search',
            placeholder='Try entering a (partial) EC number, e.g. 2.7. or 2.7.7.6',
            searchable=True,
            ),    

            html.Br(),

            html.Br(), 

            html.H4('Or switch to a different data property:'),

            dbc.RadioItems(
                options=[
                    {'label': 'Enzyme Commissions', 'value': 'ec'},
                    {'label': 'Residue Lengths', 'value': 'rl'},
                ],
                value='ec',
                id='radioitems-inline-input',
                inline=True,
            ),

            dcc.Markdown('''
            We use this column for setting the graph options.
            ''')
        ], width=5),

        dbc.Col([
            dcc.Graph(id='topenzyme_figure'),
        ]),
    ]),
    
], style={'margin-left':'10px'})

