import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output, State
import yfinance as yf
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

data = "https://github.com/roschmid/waynefoundation/raw/master/Data.csv"

df = pd.read_csv(url, sep=",")

#Layout functions

def title():
    return html.Div([html.H1("Wayne Foundation - Stock Analysis"),
                     dcc.Markdown("---"),
                     html.P(),
                     dcc.Markdown("""

Basic information here. Perhaps use a Markdown for better text

---

""")
                     ])


def tabs_layout():
    return html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='GRAPH', value='tab-1', children=[
            get_ticker_graph()]),
        dcc.Tab(label='ANALYSIS', value='tab-2', children=[
            dcc.Markdown("""We can enter some **text** to say something interesting.""")]),
        dcc.Tab(label="OTHER", value="tab-3", children=[
            dcc.Markdown("""We can enter some **text** to say something interesting.""")])
    ]),
    html.Div(id='tabs-content')
])

##TAB 1

def get_ticker_graph():
    return html.Div([
    html.H2("Historical Price Graph"),
    html.P(),
    html.Div([dcc.Input(id='input-box', type='text', placeholder="Search for Ticker Price..."), html.Button("Search", id="button")], className="rows"),
    html.Div(id='output-container-button'),
    ])

##TAB 2

#App Layout

app.layout = html.Div(children=[
    title(),
    tabs_layout()
    ])

#Callbacks

##TAB 1

@app.callback(
    Output('output-container-button', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):

    if value == None:
        info = yf.download("HABITAT.SN", period="max")
        value = "HABITAT"
    else:
        info = yf.download(str(value) + ".SN", period="max")

###Graph info

    fig = px.line(info, x=info["Close"].index.to_list(), y=info["Close"].to_list(),
                  title="Historical Price for " + str(value).upper(),
                  labels = {"x":str(value).upper(), "y": "Prices"})

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=2, label="2y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.update_layout({"plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)"
        }, hovermode="x")

###Return Layout

    return html.Div([
        dcc.Graph(
            figure=fig,
            style={"width": 1200, "height": 600},
            id="my-graph")
                    ])    


if __name__ == '__main__':
    app.run_server(debug=True)







