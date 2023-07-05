import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
# from navigation import sidebar

#external CSS stylesheets
external_stylesheets = [
    dbc.themes.SIMPLEX,
    dbc.icons.BOOTSTRAP,
    dbc.icons.FONT_AWESOME
]

#external JS scripts
external_scripts = [

]

#setup the app server
app = Dash(__name__, use_pages=True, external_scripts=external_scripts, external_stylesheets=external_stylesheets)

# server = app.server

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
                        [html.I(className=page['icon']), html.Span(f"{page['name']}")],
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

    dash.page_container
], style={'margin-left':'6rem'})

if __name__ == '__main__':
    app.run_server(debug=True)

