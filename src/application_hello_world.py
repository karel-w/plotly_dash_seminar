from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

data = pd.read_csv('../data/time_series.csv', index_col = 0)

app = Dash(__name__)

# server = app.server

app.layout = html.Div([
    html.H1('Hello world: Time series analysis'),
    dcc.Graph(id='time-series-graph'),
    dcc.RangeSlider(0, len(data), value=[0, len(data)], id='time-series-slider')
])


@callback(
    Output('time-series-graph', 'figure'),
    Input('time-series-slider', 'value')
)
def update_graph(value):
    print(value)
    df = data.iloc[value[0]:value[1]]

    fig = px.line(df)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')

