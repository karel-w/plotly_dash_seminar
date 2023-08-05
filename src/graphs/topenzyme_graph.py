import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import itertools
import matplotlib as mpl

def topenzyme_graph_basic(csv_path):
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

    #itterate over each enzyme class settings and a trace for each ec
    for ec, en, symbol, color, pos in zip(enzyme_classes, enzyme_names, markers, colors, positions):
        #main plot
        fig.add_trace(
            go.Scatter(
                x = data[data['EC'].str.startswith(f'{ec}')]['score_alpha'], y=data[data['EC'].str.startswith(f'{ec}')]['score_topm'], 
                customdata = data[data['EC'].str.startswith(f'{ec}')]['EC'].tolist(),
                hovertemplate = '<br>'.join([
                    'TopScore AF2: %{x}',
                    'TopScore TopModel: %{y}',
                    'EC: %{customdata}'
                ]),
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
                customdata = data[data['EC'].str.startswith(f'{ec}')]['EC'],
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

    #add lines for good and ok regime to subplots.
    for pos in positions:
        for val in [0.2, 0.4]:
            fig.add_shape(
                type='rect',
                x0=0, y0=0, x1=val, y1=val,
                line={
                    'color': '#A3DA8D' if val == 0.2 else '#6695be',
                    'width': 2,
                },
                layer = 'below',
                row = pos[0],
                col = pos[1],
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


def topenzyme_graph_advanced(data, cproperty='ec', minimum=10, maximum=1000, stepsize=16, cmin='#3cb44b', cmax='red'):
    #intialize figure
    fig = go.Figure()

    #colors to standard color for cproperty ec:


    #settings for each enzyme class
    enzyme_classes = np.arange(1, 8, 1)
    enzyme_names = ['Oxidoreductases', 'Transferases', 'Hydrolases', 'Lyases', 'Isomerases', 'Ligases', 'Translocases']
    markers = ['circle', 'cross', 'star', 'triangle-up', 'diamond', 'pentagon', 'square']
    colors = ['#800000', '#000075', '#e6194B', '#f58231', '#a9a9a9', '#f032e6', '#3cb44b']
    positions = [(4,1), (4, 2), (4,3), (4,4), (1,4), (2,4), (3,4)]

    ##todo block : write these out of function ##################
    values = np.linspace(minimum, maximum, stepsize)
    cmix = np.linspace(0, 1, stepsize)

    # if cproperty != 'ec':
        
    def colorFader(c1='green',c2='blue',mix=0): 
        c1=np.array(mpl.colors.to_rgb(c1))
        c2=np.array(mpl.colors.to_rgb(c2))
            
        return mpl.colors.to_hex((1-mix)*c1 + mix*c2)
        
    def find_nearest(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx], idx

    def SetColor(resl, minimum, maximum, cmin, cmax, stepsize=16):
        colors = []
        for mix in cmix:
            colors.append(colorFader(cmin, cmax, mix))
        
        arrval, idx = find_nearest(values, resl)
        
        return colors[idx]
    ##todo #######################################################

    #itterate over each enzyme class settings and a trace for each ec
    for ec, en, symbol, color, pos in zip(enzyme_classes, enzyme_names, markers, colors, positions):
        custom1 = data[data['EC'].str.startswith(f'{ec}')]['EC']
        custom2 = data[data['EC'].str.startswith(f'{ec}')]['res_length']
        #main plot
        fig.add_trace(
            go.Scatter(
                x = data[data['EC'].str.startswith(f'{ec}')]['score_alpha'], y=data[data['EC'].str.startswith(f'{ec}')]['score_topm'], 
                customdata = np.stack((custom1, custom2), axis=-1),
                hovertemplate = '<br>'.join([
                    'TopScore AF2: %{x}',
                    'TopScore TopModel: %{y}',
                    'EC: %{customdata[0]}',
                    'Residue Length: %{customdata[1]}',
                ]),
                mode='markers',
                # marker_color = color,
                marker_color = list(map(SetColor, custom2.tolist(), itertools.repeat(minimum, len(custom2)), itertools.repeat(maximum, len(custom2)), itertools.repeat(cmin, len(custom2)), itertools.repeat(cmax, len(custom2)))) if cproperty != 'ec' else color, 
                marker_symbol = symbol,
                marker_size = 8,
                name = en,
                legendrank = ec,
                legendgroup = str(ec),
            ),
        )

    #add slope to differentiate between areas
    fig.add_trace(
        go.Scatter(
            x = [0.1, 0.65],
            y = [0.1, 0.65],
            line_shape='linear',
            showlegend=False,
            line = {
                'color':'black'
            }
        )
    )

    #add squares for good and ok regime
    fig.add_shape(
        type='rect',
        x0=0.1, y0=0.1, x1=0.4, y1=0.4,
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
        x0=0.1, y0=0.1, x1=0.2, y1=0.2,
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
            'orientation':'h',
            'yanchor':'bottom',
            'xanchor':'left',
            'y': -0.15,
            'x': 0.0,
            'font' : {
                'size':20,
                'family':'Arial',
            }
        },
        xaxis_title = 'AlphaFold2 (TopScore)',
        yaxis_title = 'TopModel (TopScore)',
    )

    # we split up the axes updates in the main figure and side plots.
    # side plots first then overwrite for main plot
    # update axes main figure
    fig.update_xaxes(
        range=[0.1, 0.65],
        showticklabels=True,
        showgrid=False,
        showline=True,
        mirror=True,
        side='top',
        linecolor='black',
    )

    fig.update_yaxes(
        range=[0.1, 0.65],
        showticklabels=True,
        showgrid=False,
        side='left',
        showline=True,
        mirror=True,
        linecolor='black',
    )

    return fig