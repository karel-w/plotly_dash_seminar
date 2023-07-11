import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

dash.register_page(
    __name__,
    path='/callbacks',
    title='callbacks',
    name='callbacks',
    icon='fa-solid fa-at'
    )

all_options = {
    'Netherlands' : ['Amsterdam', 'Den Haag', 'Enschede'],
    'Germany' : ['Bonn', 'Duesseldorf', 'Koeln'],
}

layout = html.Div(children=[
    html.H1(children='Callbacks: Add a input to your application.'),
    
    dcc.Markdown('''
    Callbacks are functions that are automatically called by Dash whenever an input components property changes, in order to update some property in another component (the output).

    Essentially, they are a way to handle some input (menu, button, text field, etc) and provide this to a function which then can change the output depending on the input.

    E.g:
    '''),

    dbc.Row([
        dbc.Col([
            html.H4('1. A single callback.'),

            dcc.Markdown('''
            We describe the input and output of our function in the argument of the @callback decorator. 
            In this case the input has the component property of 'n_clicks', which counts how many times the button has been clicked. 

            The component id is that off the button, so that the button is the input to the callback.
            The output has a component property of 'children', passing the output to the children of the html.Div function with the output component id. 
            Which for html.Div is the property to set the text to display. 
            '''),

            dbc.Card([
                dbc.Col([
                    html.Br(),

                    dbc.Button('Click Me!!', id='example_button', className='d-grid gap-2 col-6 mx-auto', n_clicks=0),

                    html.Br(),

                    html.Div(id='output_button', className='text-center'),

                    html.Br(),

                    dmc.Prism(
                        language='python',
                        withLineNumbers=True,
                        children='''
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc

dbc.Button('Click Me!!', id='example_button', n_clicks=0)

html.Div(id='output_button')

@callback(
    Output(component_id = 'output_button', component_property='children'),
    Input(component_id = 'example_button', component_property='n_clicks')
)
def on_button_click(n):
    if n is None:
        return 'Please click the button!'
    else:
        return f'Clicked {n} times'

                        '''
                    ),
                ]),

            ]),
        ], width=5),

        dbc.Col([    
            html.H4('2. Multiple in- and outputs.'),

            dcc.Markdown('''
            We can add multiple inputs and outputs to the callback decorator. 
            In this case we use two inputs fields from the dash core components library. 
            We can set the default value and data type to accept. 

            In our Input decorator the component property is now set to value. 
            The first input is the first argument of the function, while the second input is the second argument to the function.
            This works similarly to the output of the function as well, where the first returned value is the first output and the second returned value the second output. 
            '''),

            dbc.Card([
                dbc.Row([
                    html.Br(), 

                    dbc.Col([
                        dcc.Markdown('''
                        Input two numbers:
                        '''),
                    ], width={'size':3, 'offset':2}),

                    dbc.Col([
                        dcc.Input(id='input_numbers1', value=1, type='number'),
                        dcc.Input(id='input_numbers2', value=2, type='number'),
                    ], width=2),
                ]),

                html.Br(),

                html.Div(id='output_numbers_sum', className='text-center'),
                html.Div(id='output_numbers_product', className='text-center'), 

                html.Br(),

                dmc.Prism(
                    language='python',
                    withLineNumbers=True,
                    children='''
from dash import html, dcc, callback, Input, Output

dcc.Input(id='input_numbers1', value=1, type='number')
dcc.Input(id='input_numbers2', value=2, type='number')

html.Div(id='output_numbers_sum', className='text-center')
html.Div(id='output_numbers_product', className='text-center')

@callback(
    Output(component_id = 'output_numbers_sum', component_property='children'),
    Output(component_id = 'output_numbers_product', component_property='children'),
    Input(component_id = 'input_numbers1', component_property='value'),
    Input(component_id = 'input_numbers2', component_property='value'),
)
def update_output_example(val1, val2):
    return f'The sum is: {val1 + val2}', f'The product is: {val1 * val2}'
                    '''),

            ]),
        ], width=5),
    ]),

    html.Br(),

    html.Br(),
    
    dbc.Row([
        dbc.Col([
            html.H4('3. Chained callbacks.'),

            dcc.Markdown('''
            Now that we understand the basics of callbacks we can start to increase the complexity. 
            Lets take a look at chained callbacks. 
            Here we can select a country, but upon country selection our city selection changes to that countries city. 

            In the first RadioItems we set the countries, and use this as an input to return a dictionary of cities in the first callback.
            The second callback takes this dictionary and displays the options in the second RadioItems function. 
            The last callback takes the value of both the first and second RadioItems to return the 'place is a city in country'. 
            '''),

            dbc.Card([
                dbc.Col([
                    html.Div('select a country:'),

                    dcc.RadioItems(
                        list(all_options.keys()),
                        'Netherlands',
                        id = 'countries-radio'
                    ),

                    html.Br(),

                    html.Div('select a city:'),

                    dcc.RadioItems(
                        id='cities-radio'
                    ),

                    html.Br(),

                    html.Div(
                        id='display-radio'
                    ),

                    html.Br(),

                    dmc.Prism(
                        language='python',
                        withLineNumbers=True,
                        children='''
from dash import html, dcc, callback, Input, Output

all_options = {
    'Netherlands' : ['Amsterdam', 'Den Haag', 'Enschede'],
    'Germany' : ['Bonn', 'Duesseldorf', 'Koeln'],
}

dcc.RadioItems(list(all_options.keys()), 'Netherlands', id = 'countries-radio'),
dcc.RadioItems(id='cities-radio')

html.Div(id='display-radio')

@callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value')
)
def set_cities_options(selected_country):
    return [{'label':i, 'value': i} for i in all_options[selected_country]]

@callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options')
)
def set_cities_value(available_options):
    return available_options[0]['value']

@callback(
    Output('display-radio', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value')
)
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )

                        '''
                    ),
                ]),

            ]),
        ], width=5),

        dbc.Col([    
            html.H4('4. State callbacks.'),

            dcc.Markdown('''
            The last example we look at is of the state callback. Normally the input of a callback is immediatly processed.
            But in some cases you might want to wait for the user to input all the information before processing the callback.

            In this example changing the text in the input box won't immediatly fire the callback, but clicking the button will. 
            The current values of the input are still passed into the callback even though they don't trigger the callback function itself.
            '''),

            dbc.Card([

                html.Br(),

                dcc.Input(id='input-state', type='text', value='Netherlands'),

                dbc.Button('Submit', id='button-state', className='me-2', n_clicks=0),

                html.Br(),

                html.Div(
                    id='output-state'
                ),

                html.Br(),

                dmc.Prism(
                    language='python',
                    withLineNumbers=True,
                    children='''
from dash import dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

dcc.Input(id='input-state', type='text', value='Netherlands')

dbc.Button('Submit', id='button-state', className='me-2', n_clicks=0)

@callback(
    Output('output-state', 'children'),
    Input('button-state', 'n_clicks'),
    State('input-state', 'value'),
)
def update_state_example(n_clicks, input):
    return u"""
        The button has been pressed {} times,
        Input is {}.
    """".format(n_clicks, input)
                    '''),

            ]),
        ], width=5),    
    ]),
], style={'margin-left':'10px'})

#single callbacks
@callback(
    Output(component_id = 'output_button', component_property='children'),
    Input(component_id = 'example_button', component_property='n_clicks')
)
def on_button_click(n):
    if n is None:
        return 'Please click the button!'
    else:
        return f'Clicked {n} times'

#multiple callbacks
@callback(
    Output(component_id = 'output_numbers_sum', component_property='children'),
    Output(component_id = 'output_numbers_product', component_property='children'),
    Input(component_id = 'input_numbers1', component_property='value'),
    Input(component_id = 'input_numbers2', component_property='value'),
)
def update_output_example(val1, val2):
    return f'The sum is: {val1+val2}', f'The product is: {val1*val2}'

#chained callbacks
@callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value')
)
def set_cities_options(selected_country):
    return [{'label':i, 'value': i} for i in all_options[selected_country]]

@callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options')
)
def set_cities_value(available_options):
    return available_options[0]['value']

@callback(
    Output('display-radio', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value')
)
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )

#state callbacks
@callback(
    Output('output-state', 'children'),
    Input('button-state', 'n_clicks'),
    State('input-state', 'value'),
)
def update_state_example(n_clicks, input):
    return u'''
        The button has been pressed {} times,
        Input is "{}".
    '''.format(n_clicks, input)