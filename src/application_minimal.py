from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.graph_objects as go

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

app = Dash(__name__)

@callback(
    Output('color_store', 'value'),
    Input('submit_button', 'n_clicks'),
    State('color_picker', 'value'),
)
def update_colors(n_clicks, colval):
    return colval

#Normally i import this function from another file
def create_figure(radio_val, color='pink'):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=[0, 1, 2, 3, 4] if radio_val == 'option1' else [0, 100, 200, 300, 400], 
            y=[0, 1, 4, 9, 16], 
            mode='markers', 
            marker_color=color,
        )
    )
    return fig

@callback(
    Output('my_figure', 'figure'),
    Input('radio', 'value'),
    Input('color_store', 'value'),
)
def update_figure(radio_selection, color_selection):
    print('color selected:', color_selection)

    fig = create_figure(radio_val=radio_selection, color=color_selection)

    return fig

@callback(
    Output('card', 'children'),
    Input('radio', 'value'),
)
def display_card(radio_option):
    if radio_option == 'option2':
        component = dbc.Card([
            dbc.CardBody([
                html.H4('There is some text here'),

                dmc.ColorPicker(id="color_picker", format="hex", value="#ff0000"),

                html.Button('Submit', id='submit_button', n_clicks=0),
            ])
        ])

        return component
    else:
        return []

app.layout = html.Div([
    dcc.Store(id='color_store'),
    
    dcc.Graph(id='my_figure'),

    dbc.RadioItems(
        options=[
            {'label': 'option1', 'value': 'option1'},
            {'label': 'option2', 'value': 'option2'},
        ],
        value='option1',
        id='radio',
        inline=True,
    ),

    html.Div(id='card'),

])



if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')

