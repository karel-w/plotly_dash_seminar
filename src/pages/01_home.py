import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
dash.register_page(
    __name__,
    path='/',
    title='home',
    name='home',
    icon='fa-solid fa-house'
    )
layout = html.Div(children=[
    html.H1(children='Interactive Graphs and Dashboards for Data Science Projects'),

    html.Div(
        [
            html.Img(src='assets/Karel_vdW.jpg', alt='headshot', style={'width':'6%', 'float': 'left', 'margin-right':'10px'}),

            dcc.Markdown(''' 
                Hello, everyone! I'm Karel van der Weg, a fellow HDS-LEE doctoral researcher at the Juelich Supercomputing Centre and Institute for Bio- and Geosciences 4: Bioinformatics.
                My primary focus revolves around machine learning methods for understanding Proteins.

                During my work, I've come across a notable observation—the data we work with is becoming increasingly complex.
                As researchers, when we explore new publications, we often find ourselves wanting to delve deeper into the data and understand the underlying processes.
                For instance, have you ever wondered why certain values appear on a plot?
                Typically, this involves navigating through supporting information, hoping to find the relevant details in a clear and structured manner.

                I believe that as a research community, we have the potential to enhance how we present complex information to readers of scientific papers.
                We've already witnessed some progress in the machine learning community, where interactive resources have allowed us to explore machine learning models with greater ease.
                My goal is to extend this development to the life sciences and, hopefully, to your specific scientific field.

                In this course, I aim to introduce you to the power of interactive graphs and dashboards using Plotly and Dash.
                By mastering these tools, you will be able to present your scientific data in a more intuitive and visually appealing manner.
                We will cover the techniques necessary to create captivating visualizations that invite exploration and facilitate a deeper understanding of your data.

                Joining this course will provide you with the knowledge and skills to bridge the gap between complex data and effective communication.
                Together, we will work towards enhancing the impact of your research by transforming it into compelling visual narratives.
            ''', style={'display': 'inline'}),
        ], style = {'float':'right'}
    ),

    html.H3(children='Course content'),

    dcc.Markdown('''
    This course is tailor-made for researchers and scientists who are eager to elevate their data visualization capabilities.
    Whether you're in the life, energy or earth, this course will equip you with the basic tools needed to captivate your audience and maximize the impact of your research.
    
    In this course you will learn to:
    
    1. Develop expertise in creating visually captivating interactive graphs and dashboards.
    2. Gain proficiency in leveraging Plotly and Dash to present complex data in an intuitive and user-friendly format.
    3. Enhance your ability to communicate scientific findings effectively through engaging visual narratives.
    4. Acquire skills to transform your research output into immersive and interactive experiences.
    5. Empower yourself to bridge the gap between complex data and its comprehension, unlocking greater impact for your work.

    '''),

], style={'margin-left':'10px'})