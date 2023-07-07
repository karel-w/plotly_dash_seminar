import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def topenzyme_graph(csv_path):
    data = pd.read_csv(csv_path)

    #create the subplot layout
    fig = make_subplots(
        rows=4, cols=4,
        specs = [
            [{'rowspan':3, 'colspan':3}, None, None, {}],
            [None, None, None, {}],
            [None, None, None, {}],
            [{}, {}, {}, {}],
        ],
        print_grid=False,
        vertical_spacing = 0,
        horizontal_spacing = 0,
    )

    #settings for each enzyme class
    enzyme_classes = np.arange(1, 8, 1)
    enzyme_names = ['Oxidoreductases', 'Transferases', 'Hydrolases', 'Lyases', 'Isomerases', 'Ligases', 'Translocases']
    markers = ['circle', 'cross', 'star', 'triangle-up', 'diamond', 'pentagon', 'square']
    colors = ['#800000', '#000075', '#e6194B', '#f58231', '#a9a9a9', '#f032e6', '#3cb44b']
    positions = [(4,1), (4, 2), (4,3), (4,4), (1,4), (2,4), (3,4)]

    #add lines for good and ok regime to subplots, we do this first to have the traces below the data points
    line_trace1 = {
        'type':'scatter',
        'x':[0.2, 0.2],
        'y':[0, 0.2],
        'line_shape':'linear',
        'showlegend':False,
        'line' : {'color':'#A3DA8D'},
    }

    line_trace2 = {
        'type':'scatter',
        'x':[0, 0.2],
        'y':[0.2, 0.2],
        'line_shape':'linear',
        'showlegend':False,
        'line' : {'color':'#A3DA8D'},
    }

    line_trace3 = {
        'type':'scatter',
        'x':[0.4, 0.4],
        'y':[0, 0.4],
        'line_shape':'linear',
        'showlegend':False,
        'line' : {'color':'#6695be'},
    }

    line_trace4 = {
        'type':'scatter',
        'x':[0, 0.4],
        'y':[0.4, 0.4],
        'line_shape':'linear',
        'showlegend':False,
        'line' : {'color':'#6695be'},
    }

    for pos in positions:
        fig.append_trace(line_trace1, pos[0], pos[1])
        fig.append_trace(line_trace2, pos[0], pos[1])
        fig.append_trace(line_trace3, pos[0], pos[1])
        fig.append_trace(line_trace4, pos[0], pos[1])

    #itterate over each enzyme class settings and a trace for each ec
    for ec, en, symbol, color, pos in zip(enzyme_classes, enzyme_names, markers, colors, positions):
        #main plot
        fig.add_trace(
            go.Scatter(
                x = data[data['EC'].str.startswith(f'{ec}')]['score_alpha'], y=data[data['EC'].str.startswith(f'{ec}')]['score_topm'], 
                mode='markers',
                marker_color = color,
                marker_symbol = symbol,
                marker_size = 8,
                name = en,
                legendrank = ec,
                legendgroup = str(ec),
            ),
            row = 1,
            col = 1
        )
        # side plots
        fig.add_trace(
            go.Scatter(
                x = data[data['EC'].str.startswith(f'{ec}')]['score_alpha'], y=data[data['EC'].str.startswith(f'{ec}')]['score_topm'], 
                mode='markers',
                marker_color = color,
                marker_symbol = symbol,
                marker_size = 6,
                name = en,
                legendrank = ec,
                legendgroup = str(ec),
                showlegend=False,
            ),
            row = pos[0],
            col = pos[1],
        )

    #add slope to differentiate between areas
    slope_trace = {
        'type':'scatter',
        'x':[0, 1],
        'y':[0, 1],
        'line_shape':'linear',
        'showlegend':False,
        'line' : {'color':'black'},
    }

    fig.append_trace(slope_trace, 1, 1)
    for pos in positions:
        fig.append_trace(slope_trace, pos[0], pos[1])


    #add squares for good and ok regime
    fig.add_shape(
        type='rect',
        x0=0, y0=0, x1=0.4, y1=0.4,
        fillcolor='#6695be',
        line={
            'color':'#6695be'
        },
        layer='below',
        label = {
            'text':'good quality', 'textposition':'top left',
            'font':{'family':'arial', 'size': 8},
        },
    )
    fig.add_shape(
        type='rect',
        x0=0, y0=0, x1=0.2, y1=0.2,
        fillcolor='#A3DA8D',
        line={
            'color':'#A3DA8D'
        },
        layer='below',
        label = {
            'text':'high quality', 'textposition':'top left',
            'font':{'family':'arial', 'size': 8},
        },
    )

    # update layout
    fig.update_layout(
        width=800,
        height=800,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        font = {
            'family':'Arial',
            'size':20,
            'color':'black',
        },
        legend_tracegroupgap = 3,
        legend = {
            'orientation':'v',
            'yanchor':'bottom',
            'xanchor':'right',
            'y': 0.28,
            'x': 0.7,
            'font' : {
                'size':14,
                'family':'Arial',
            }
        },
        xaxis_title = 'AlphaFold2 (TopScore)',
        yaxis_title = 'TopModel (TopScore)',
    )

    # we split up the axes updates in the main figure and side plots.
    # side plots first then overwrite for main plot
    fig.update_xaxes(
        range=[0.1, 0.65],
        showline=True,
        showgrid=False,
        ticks='',
        showticklabels=False,
        mirror=True,
        linecolor='black',
    )

    fig.update_yaxes(
        range=[0.1, 0.65],
        ticks='',
        showticklabels=False,
        showline=True,
        showgrid=False,
        mirror=True,
        linecolor='black',
    )

    # update axes main figure
    fig.update_xaxes(
        range=[0.1, 0.65],
        showticklabels=True,
        showline=True,
        mirror=True,
        side='top',
        linecolor='black',
        row=1,
        col=1,
    )

    fig.update_yaxes(
        range=[0.1, 0.65],
        showticklabels=True,
        side='left',
        showline=True,
        mirror=True,
        linecolor='black',
        row=1,
        col=1,
    )

    return fig

# fig.write_image('topenzyme_graph_test.png')