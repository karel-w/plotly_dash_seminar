import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(
    __name__,
    path='/deployment-panyw',
    title='deployment',
    name='deployment',
    icon='fa-solid fa-python'
    )

layout = html.Div(children=[
    html.H1(children='Deployment.'),

    dcc.Markdown('''
    Dash applications are easy to implement on existing systems. Two popular hosts for dashboards are [heroku](https://www.heroku.com/) and [pythonanywhere](https://www.pythonanywhere.com/).
    Pythonanywhere has a european sub-company that hosts the data in Germany as per GDPR. This is accessible through [https://eu.pythonanywhere.com](https://eu.pythonanywhere.com).
                 
    In this tutorial we will follow pythonanywhere.com to host our dashboard. Note that using the free services often limits your possibilites for a URL.
    For example this app is currently hosted at kvanderweg.eu.pythonanywhere.com. If you are a paying user the company can host the dashboard and you can implement it in your own website.
    You could also fully host the app on your own webserver, but setting this up usually takes a bit of time to figure out and is heavily environment dependant.
    
    I only have experience with deploying the app with Apache on our webserver. If your situation is similar feel free to mail me for help. 
                 
server = app.server


if __name__ == "__main__":
    app.run_server(debug=True)

'''),

    html.H3('WSGI files'),

    dmc.Prism(
        language='python',
        withLineNumbers=True,
        children='''
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys

# add your project directory to the sys.path
project_home = '/home/kvanderweg/topenzyme/src'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from app import server as application 
'''),
    
], style={'margin-left':'10px'})

