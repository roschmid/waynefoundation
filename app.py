import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output, State
import yfinance as yf
import plotly.express as px
import pandas as pd
import dash_table
import dash_auth
import json
import numpy as np

external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/minty/bootstrap.min.css"]

with open("usr.json", "r") as file:
    USER_PASS = json.load(file)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Orbis Investments"

auth = dash_auth.BasicAuth(
    app,
    USER_PASS)

server = app.server

data = "https://raw.githubusercontent.com/roschmid/waynefoundation/master/Data.csv"

df = pd.read_csv(data, sep=",")
PAGE_SIZE = 25

#Layout functions

def title():
    return html.Div([html.H1("Orbis Investments - Stock Market Workshop"),
                     dcc.Markdown("---"),
                     html.P(),
                     dcc.Markdown("""
Welcome to the Orbis Investments' **Stock Market Workshop** (SMW),
created by Rafael Schmidt.
> **What is the SMW?**\n
The SMW is a place where you can analyze and prepare your personal portfolio
to invest in Chilean stocks.\n
Orbis Investments provides historical data on all of the stocks in the Chilean
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
        dcc.Tab(label="Orbis Academy", value="tab-3", children=[orbis_academy()]),
        dcc.Tab(label="What's New?", value="tab-4", children=[
            whats_new()])
    ]),
    html.Div(id='tabs-content')
])

##TAB 1

def get_ticker_graph():
    return html.Div([
    html.H2("Historical Price Graph"),
    html.P(),
    html.Div([dcc.Input(id='input-box', type='text', placeholder="Search Ticker..."),
              html.Button("Search", id="button", style={"backgroundColor": "white", 
                                                        "color": "black", "border": "1px solid grey",
                                                        "padding": "3px 38px",
                                                        "textAlign": "center", "textDecoration": "none",
                                                        "display": "inline-block", "fontSize": "16px"})], className="rows"),
    html.Div(id='output-container-button'),
    ])

##TAB 2

def get_stock_table():
    return html.Div([
    html.H2("Individual Stock Analysis"),
    dcc.Markdown("""---"""),
    html.Div([html.P(children="Price-Earning Ratio:", id='pe-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='pe-min', type='number', placeholder="Min.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("to", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='pe-max', type='number', placeholder="Max.", value=df["PE"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    html.Div([html.P(children="Book Value Ratio:", id='bv-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='bv-min', type='number', placeholder="Min.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("to", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='bv-max', type='number', placeholder="Max.", value=df["BV"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    html.Div([html.P(children="Min. Years of Uninterrupted Dividends:", id='unint-div-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='unint-div', type='number', placeholder="Min.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})]),
    html.Div([html.P(children="Compare your favorite stocks:", id="multi-select-label", style={"display":"inline-block", "margin": "10px 0px 0px 0px"}),
                     dcc.Dropdown(
                         id="ticker-dropdown",
                         options=[
                             {'label': i, 'value': i} for i in df["NEMO"].unique()
                         ],
                         multi=True,
                         placeholder="Filter by Ticker...",
                         style={"width":500}                         
                         )]),
    dcc.Markdown("""---"""),
    html.Div([
        html.P(""),
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
    )])])

##TAB 3

def orbis_academy():
    return html.Div([
        html.H2("Orbis Academy"),
        dcc.Markdown("""
Here you will learn the most important  concepts to evaluate your investments and portfolios from a **value investing** standpoint."""),
        html.Table([
            html.Tr([html.Td(["Price/Earning Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The price-to-earnings ratio or P/E is one of the most widely-used stock analysis tools used by investors and analysts for determining stock valuation.
The P/E Ratio can be viewed sa the number of years it takes for the company to earn back the price you pay for the stock. Recommended P/E Ratio < 15.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "15px", "textAlign": "left"})]),
            html.Tr([html.Td(["Book Value Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value.
It's calculated by dividing the company's stock price per share by its book value per share (BVPS).
An asset's book value is equal to its carrying value on the balance sheet, and companies calculate it netting the asset against its accumulated depreciation.
Recommended B/V < 2.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "15px", "textAlign": "left"})]),
            html.Tr([html.Td(["Current Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The current ratio is a liquidity ratio that measures a company's ability to pay short-term obligations or those due within one year. Recommended ratio > 1.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "15px", "textAlign": "left"})])
            ])
        ])

##TAB 4

def whats_new():
    return html.Div([
    html.H2("What's New?"),
    dcc.Markdown("""
- 8/08/2020: Select your favorite stocks and compare!
- 7/08/2020: Added password protection and new columns for Stock Analysis section.
- 6/08/2020: Introducing, the **Orbis Academy!**
- 5/08/2020: Added **Price/Earning**, **Book Value**, and **Uninterrupted Dividend** filters to begin with your portfolio analysis. 
- 4/08/2020: Added the **"Price" column** in the Stock Analysis section
- 2/08/2020: **Official release** of the Orbis Investments' SMW!""")])

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
    Output('datatable-paging', 'data'),
    [Input('datatable-paging', 'page_current'),
     Input('datatable-paging', 'page_size'),
     Input('datatable-paging', 'sort_by'),
     Input('pe-min', 'value'),
     Input("pe-max", "value"),
     Input("bv-min", "value"),
     Input("bv-max", "value"),
     Input("filter-input", "value"),
     Input("unint-div", "value"),
     Input("ticker-dropdown", "value")])
def update_table(page_current, page_size, sort_by, pe_min, pe_max, bv_min, bv_max, filter_string, min_unint_div, ticker_dropdown):

    # Filter

    max_div = df["UNINT. DIV."].max()

    num_df = df[(df["PE"].between(pe_min, pe_max)) &
                (df["BV"].between(bv_min, bv_max)) &
                (df["UNINT. DIV."].between(min_unint_div, max_div))] #to use OR, change "&" for "|"
    final_df = num_df[num_df.apply(lambda row: row.str.contains(filter_string.upper(), regex=False).any(), axis=1)]

    if ticker_dropdown is None:
        filtered_df = final_df
    else:
        filtered_df = final_df[final_df["NEMO"].str.contains("|".join(ticker_dropdown))]

    # Sort if necessary
    if len(sort_by):
        filtered_df = filtered_df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )

    return filtered_df.iloc[
           page_current * page_size:(page_current + 1) * page_size
           ].to_dict('records')

#Main

if __name__ == '__main__':
    app.run_server(debug=True)
