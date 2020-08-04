import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output, State
import yfinance as yf
import plotly.express as px
import pandas as pd
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

data = "https://raw.githubusercontent.com/roschmid/waynefoundation/master/Data.csv"

df = pd.read_csv(data, sep=",")
PAGE_SIZE = 25

#Layout functions

def title():
    return html.Div([html.H1("Wayne Foundation - Stock Market Workshop"),
                     dcc.Markdown("---"),
                     html.P(),
                     dcc.Markdown("""
Welcome to the Wayne Foundation's **Stock Market Workshop** (SMW),
created by Rafael Schmidt.
> **What is the SMW?**\n
The SMW is a place where you can analyze and prepare your personal portfolio
to invest in Chilean stocks.\n
Wayne Foundation provides historical data on all of the stocks in the Chilean
market, such as price, dividend yield, PE ratio, among others.\n
Furthermore, you will be able to find information that is not
available even in the Chilean Stock Exchange.\n
For more information, do not hesitate to contact us via [GitHub](https://github.com/roschmid/waynefoundation). \n
---
""")
                     ])


def tabs_layout():
    return html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Historical Graph', value='tab-1', children=[
            get_ticker_graph()]),
        dcc.Tab(label='Stock Analysis', value='tab-2', children=[
            get_stock_table()]),
        dcc.Tab(label="What's New?", value="tab-3", children=[
            whats_new()])
    ]),
    html.Div(id='tabs-content')
])

##TAB 1

def get_ticker_graph():
    return html.Div([
    html.H2("Historical Price Graph"),
    html.P(),
    html.Div([dcc.Input(id='input-box', type='text', placeholder="Search Ticker..."), html.Button("Search", id="button")], className="rows"),
    html.Div(id='output-container-button'),
    ])

##TAB 2

def get_stock_table():
    return html.Div([
    html.H2("Individual Stock Analysis"),
    dcc.Input(value='', id='filter-input', placeholder='Search for Ticker...', debounce=False),
    dash_table.DataTable(
        id='datatable-paging',
        columns=[
            {"name": i, "id": i} for i in df.columns  # sorted(df.columns)
        ],
        page_current=0,
        page_size=PAGE_SIZE,
        page_action='custom',

        sort_action='custom',
        sort_mode='single',
        sort_by=[]
    )])

##TAB 3

def whats_new():
    return html.Div([
    html.H2("What's New?"),
    dcc.Markdown("""
- 4/08/2020: Added the **"Price" column** in the Stock Analysis section
- 2/08/2020: **Official release** of the Wayne Foundation's SMW!""")])

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

##TAB 2

@app.callback(
    dash.dependencies.Output('datatable-paging', 'data'),
    [dash.dependencies.Input('datatable-paging', 'page_current'),
     dash.dependencies.Input('datatable-paging', 'page_size'),
     dash.dependencies.Input('datatable-paging', 'sort_by'),
     dash.dependencies.Input('filter-input', 'value')])
def update_table(page_current, page_size, sort_by, filter_string):

    # Filter
    dff = df[df.apply(lambda row: row.str.contains(filter_string.upper(), regex=False).any(), axis=1)]
    # Sort if necessary
    if len(sort_by):
        dff = dff.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )

    return dff.iloc[
           page_current * page_size:(page_current + 1) * page_size
           ].to_dict('records')

#Main

if __name__ == '__main__':
    app.run_server(debug=True)
