
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
    x=df.Date,
    y=df['AAPL.High'],
    name = "AAPL High",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

trace_low = go.Scatter(
    x=df.Date,
    y=df['AAPL.Low'],
    name = "AAPL Low",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)

data = [trace_high,trace_low]

layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)

fig = dict(data=data, layout=layout)

# Now here's the Dash part:

dash.layout = html.Div([
    dcc.Graph(id='my-graph', figure=fig)
])