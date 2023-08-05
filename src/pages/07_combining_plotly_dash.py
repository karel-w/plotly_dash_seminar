import dash
from dash import html, dcc, callback, Input, Output, State, ALL
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

@callback(
    Output('dynamic_search', 'options'),
    Input('dynamic_search', 'search_value'),
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in dict_list if search_value.casefold() in o['label'].casefold()]

#################################################################################################
##### Color Pickers #############################################################################

swatches = [
    '#800000', '#000075', '#e6194B', '#f58231', '#a9a9a9', '#f032e6', '#3cb44b'
]

# colpick1 = dmc.ColorPicker(id={'type':'color_one'}, format='hex', swatchesPerRow=7, withPicker=True, swatches=swatches, value='#73cd0b')
# # colpick2 = dmc.ColorPicker(id={'type':'color_two', 'index':'colindex'}, swatchesPerRow=7, withPicker=True, swatches=swatches, value='#f09721')

@callback(
    Output('color_store', 'value'),
    Input('submit_button', 'n_clicks'),
    State('color_picker1', 'value'),
    State('color_picker2', 'value'),
    State('resl-slider', 'value'),
)
def update_colors(n_clicks, colval1, colval2, ranges):
    return colval1, colval2, ranges

#################################################################################################
##### TopEnzyme Figure ##########################################################################
@callback(
    Output('topenzyme_figure', 'figure'),
    Input('dynamic_search', 'value'),
    Input('ec_resl_radio', 'value'),
    Input('color_store', 'value'),
)
def update_figure(search_value, data_property, stored_col):
    # print('color_selected:', stored_col)
    # print(ranges)
    
    if data_property == 'rl':
        col1 = stored_col[0]
        col2 = stored_col[1]
        range_start = stored_col[2][0]
        range_end = stored_col[2][1]
    else:
        col1 = 'red'
        col2 = 'blue'
        range_start = 100
        range_end = 1000

    if search_value:
        if search_value.count('.') < 3:
            df = data[data['EC'].str.startswith(search_value + '.')]
        else:
            df = data[data['EC'].str.startswith(search_value)]
        
        fig = topenzyme_graph_advanced(df, cproperty=data_property, cmin=col1, cmax=col2, minimum=range_start, maximum=range_end)

    else:
        df = data
        fig = topenzyme_graph_advanced(df, cproperty=data_property, cmin=col1, cmax=col2, minimum=range_start, maximum=range_end)

    return fig

#################################################################################################
##### Residue Length Card setings ###############################################################
@callback(
    Output('reslength_card', 'children'),
    Input('ec_resl_radio', 'value'),
)
def reslength_card_options(radio_option):
    if radio_option == 'rl':
        component = dbc.Card([
            dbc.CardBody([
                html.H4('Settings panel'),

                html.Br(),

                html.H6('Sequence range'),

                dcc.RangeSlider(0, 2000, value=[100, 1000], id='resl-slider',
                    marks={
                        0: '0',
                        250: '250',
                        500: '500',
                        750: '750',
                        1000: '1000',
                        1250: '1250',
                        1500: '1500',
                        1750: '1750',
                        2000: '2000',
                    }
                ),

                html.Br(),

                html.H6('Color spectrum'),

                dbc.Row([
                    dbc.Col([
                        dmc.Text('select color one:', size='xs'),
                        
                        dmc.ColorPicker(id="color_picker1", format="hex", swatches=swatches, value="#ff0000"),

                        html.Button('Submit', id='submit_button', n_clicks=0),

                    ], width=6),

                    dbc.Col([
                        dmc.Text('select color two:', size='xs'),

                        dmc.ColorPicker(id='color_picker2', format='hex', swatches=swatches, value='#0000ff'),
                    ], width=6),
                ])

                
            ])
        ])

        return component
    else:
        return []

layout = html.Div(children=[
    html.H1(children='Combining dash and plotly.'),

    dcc.Store(id = 'color_store'),

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
                id='ec_resl_radio',
                inline=True,
            ),

            html.Div(id='reslength_card'),

            html.Br(),

            html.H4('We can even show structures: click a graph point'),

            # dbc.Row([
            #     dbc.Col([

            #     ], width=6),

            #     dbc.Col([

            #     ], width=6),
            # ])

            dcc.Markdown('''
            We use this column for setting the graph options.
            ''')
        ], width=5),

        dbc.Col([
            dcc.Graph(id='topenzyme_figure'),
        ]),
    ]),
    
], style={'margin-left':'10px'})

