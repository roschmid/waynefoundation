###NEXT STEPS:
#CREATE RECOMMENDED STOCKS BASED ON ALGORITHM (SEND TO MAIL AND FOLLOW-UP THE DIFFERENT RECOMMENDED PORTFOLIOS)
#USE PORTFOLIO ALREADY SAVED AND UPLOAD TO GIT. USE THAT DF FOR COMPARISON AND RETURN'S SAKE!
#3) COMPLETE SPANISH/ENGLISH VERSION
#4) ADJUST FOR MOBILE VERSION
#5) GIT UPDATE STOCK INFO (Update .csv by parts)
#6) FIND A WAY TO MONETIZE THIS AND MAKE IT PUBLIC.
#CLEAN CODE

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
import dash_bootstrap_components as dbc
import urllib.parse
from pages import (title,
                   orbis_academy,
                   whats_new)


#Opening variables

external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/minty/bootstrap.min.css"]

with open("usr.json", "r") as file:
    USER_PASS = json.load(file)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
app.title = "Orbis Investments"

auth = dash_auth.BasicAuth(
    app,
    USER_PASS)

server = app.server

data = "https://raw.githubusercontent.com/roschmid/waynefoundation/master/assets/Data.csv"

df = pd.read_csv(data, sep=",")

def get_ranking():

    pe_rank = df["PE"].rank(ascending=True)
    bv_rank = df["BV"].rank(ascending=True)
    unint_div_rank = df["UNINT. DIV."].rank(ascending=False)
    div_rank = df["HIST. DIV. YIELD (%)"].rank(ascending=False)
    op_margin_rank = df["OP. MARGIN (%)"].rank(ascending=False)
    roic_rank = df["ROIC (%)"].rank(ascending=False)
    current_ratio_rank = df["CURRENT RATIO"].rank(ascending=False)

    rank = pe_rank + (bv_rank*0.25) + (unint_div_rank*0.5) + div_rank + (op_margin_rank*0.5) + (roic_rank*0.5) + (current_ratio_rank*0.25)

    filtered_rank = rank.rank(ascending=True)

    return filtered_rank

df["ORBIS RANKING"] = get_ranking()
    
PAGE_SIZE = 25

#Layout functions

def tabs_layout():
    return html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Historical Graph', value='tab-1', children=[
            get_ticker_graph()]),
        dcc.Tab(label='Stock Analysis', value='tab-2', children=[
            get_stock_table()]),
        dcc.Tab(label="Orbis Academy", value="tab-3", children=[orbis_academy.info()]),
        dcc.Tab(label="What's New?", value="tab-4", children=[
            whats_new.info()])
    ],
             colors={
                 "border": '#d6d6d6',
                 "primary": 'green',
                 "background": '#f9f9f9', }),
    html.Div(id='tabs-content')
])

def tabs_layout_spanish():
    return html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Gráfico Histórico', value='tab-1', children=[
            get_ticker_graph_spanish()]),
        dcc.Tab(label='Análisis de Acciones', value='tab-2', children=[
            get_stock_table_spanish()]),
        dcc.Tab(label="Academia Orbis", value="tab-3", children=[orbis_academy.info_spanish()]),
        dcc.Tab(label="Novedades", value="tab-4", children=[
            whats_new.info_spanish()])
    ],
             colors={
                 "border": '#d6d6d6',
                 "primary": 'green',
                 "background": '#f9f9f9', }),
    html.Div(id='tabs-content')
])

##TAB 1

def get_ticker_graph():
    return html.Div([
    html.H2("Historical Price Graph"),
    dcc.Markdown("""---"""),
    html.Div([dcc.Input(id='input-box', type='text', placeholder="Search Ticker..."),
              html.Button("Search", id="button", style={"backgroundColor": "white", 
                                                        "color": "black", "border": "1px solid grey",
                                                        "padding": "3px 38px", "margin": "0px 0px 0px 10px",
                                                        "textAlign": "center", "textDecoration": "none",
                                                        "display": "inline-block", "fontSize": "16px"})], className="rows"),
    html.Div(id='output-container-button'),
    ])

def get_ticker_graph_spanish():
    return html.Div([
    html.H2("Gráfico Histórico del Precio"),
    dcc.Markdown("""---"""),
    html.Div([dcc.Input(id='input-box', type='text', placeholder="Buscar Nemo..."),
              html.Button("Buscar", id="button", style={"backgroundColor": "white", 
                                                        "color": "black", "border": "1px solid grey",
                                                        "padding": "3px 38px", "margin": "0px 0px 0px 10px",
                                                        "textAlign": "center", "textDecoration": "none",
                                                        "display": "inline-block", "fontSize": "16px"})], className="rows"),
    html.Div(id='output-container-button'),
    ])

##TAB 2

def get_stock_table():
    
    return html.Div([
    html.H2("Individual Stock Analysis"),
    dcc.Markdown("""---"""),

#Value Filters
    
    html.Div([
        dbc.Button("⭳ Value Filters",
                   id="value-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
        dbc.Collapse(
            html.Div([
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
    html.Div([html.P(children="Historical Dividend Yield (5 yr):", id='hist-div-yield-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='hist-div-yield', type='number', placeholder="Min. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})]),
    html.Div([html.P(children="Min. Years of Uninterrupted Dividends:", id='unint-div-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='unint-div', type='number', placeholder="Min.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})])]),
    id="value-collapse")]),

#Return Ratio Filters

    html.Div([
        dbc.Button("⭳ Return Ratio Filters",
                   id="return-ratio-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
            dbc.Collapse(
            html.Div([
    html.Div([html.P(children="Return on Invested Capital (ROIC):", id='roic-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='roic-min', type='number', placeholder="Min. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    html.Div([html.P(children="Return on Invested Equity (ROE):", id='roe-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='roe-min', type='number', placeholder="Min. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    html.Div([html.P(children="Operating Margin:", id='op-margin-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='op-margin-min', type='number', placeholder="Min. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    ]),
    id="return-ratio-collapse")]),

#Financial Filters

    html.Div([
        dbc.Button("⭳ Financial Filters",
                   id="financial-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
        dbc.Collapse(
            html.Div([
    html.Div([html.P(children="Current Ratio:", id='current-ratio-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='current-ratio-min', type='number', placeholder="Min.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("to", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='current-ratio-max', type='number', placeholder="Max.", value=df["CURRENT RATIO"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    ]),
    id="financial-collapse")]),
    
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
        dcc.Input(value='', id='filter-input', placeholder='Search for Ticker...', debounce=False, style={"margin":"0px 0px 1px -15px"}),
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
        sort_by=[],
        css=[
            {
        'selector': 'table',
        'rule': 'width: 100%;'
        },
],
    ),
        html.A(
            "Download Data",
            id="download-link",
            download="Orbis-Investments-Screener.csv",
            href="",
            style={"margin":"0px 0px 0px -15px"},
            target="_blank")
        ])])  

def get_stock_table_spanish():
    
    return html.Div([
    html.H2("Análisis Individual"),
    dcc.Markdown("""---"""),

#Value Filters
    
    html.Div([
        dbc.Button("⭳ Filtros de Valor",
                   id="value-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
        dbc.Collapse(
            html.Div([
    html.Div([html.P(children="Ratio Precio-Utilidad:", id='pe-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='pe-min', type='number', placeholder="Mín.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("a", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='pe-max', type='number', placeholder="Máx.", value=df["PE"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    html.Div([html.P(children="Ratio Valor Libro:", id='bv-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='bv-min', type='number', placeholder="Mín.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("a", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='bv-max', type='number', placeholder="Máx.", value=df["BV"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    html.Div([html.P(children="Retorno de Dividendos Histórico (5 años):", id='hist-div-yield-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='hist-div-yield', type='number', placeholder="Mín. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})]),
    html.Div([html.P(children="Años de Dividendos Ininterrumpidos:", id='unint-div-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='unint-div', type='number', placeholder="Mín.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})])]),
    id="value-collapse")]),

#Return Ratio Filters

    html.Div([
        dbc.Button("⭳ Filtros de Retornos",
                   id="return-ratio-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
            dbc.Collapse(
            html.Div([
    html.Div([html.P(children="Retorno sobre el Capital Invertido (ROIC):", id='roic-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='roic-min', type='number', placeholder="Mín. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    html.Div([html.P(children="Retorno sobre el Patrimonio (ROE):", id='roe-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='roe-min', type='number', placeholder="Mín. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    html.Div([html.P(children="Margen Operativo:", id='op-margin-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='op-margin-min', type='number', placeholder="Mín. (%)", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              ]),
    ]),
    id="return-ratio-collapse")]),

#Financial Filters

    html.Div([
        dbc.Button("⭳ Filtros Financieros",
                   id="financial-collapse-button",
                   className="mb-3",
                   color="primary",
                   style={"width":"100%", "textAlign":"left"}
                   ),
        dbc.Collapse(
            html.Div([
    html.Div([html.P(children="Razón Líquida:", id='current-ratio-label', style={"display":"inline-block", "margin": "0px 0px 0px 0px"}),
              dcc.Input(id='current-ratio-min', type='number', placeholder="Mín.", value=0, style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"}),
              html.P("a", style={"display":"inline-block", "margin": "0px 0px 0px 10px"}),
              dcc.Input(id='current-ratio-max', type='number', placeholder="Máx.", value=df["CURRENT RATIO"].max(), style={"width":100, "height":20, "display":"inline-block", "margin": "0px 0px 0px 10px"})
              ]),
    ]),
    id="financial-collapse")]),
    
    html.Div([html.P(children="Compara tus acciones favoritas:", id="multi-select-label", style={"display":"inline-block", "margin": "10px 0px 0px 0px"}),
                     dcc.Dropdown(
                         id="ticker-dropdown",
                         options=[
                             {'label': i, 'value': i} for i in df["NEMO"].unique()
                         ],
                         multi=True,
                         placeholder="Filtra por Nemo...",
                         style={"width":500}                         
                         )]),
    dcc.Markdown("""---"""),
    html.Div([
        html.P(""),
        dcc.Input(value='', id='filter-input', placeholder='Buscar Nemo...', debounce=False, style={"margin":"0px 0px 1px -15px"}),
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
        sort_by=[],
        css=[
            {
        'selector': 'table',
        'rule': 'width: 100%;'
        },
],
    ),
        html.A(
            "Descargar Data",
            id="download-link",
            download="Orbis-Investments-Screener.csv",
            href="",
            style={"margin":"0px 0px 0px -15px"},
            target="_blank")
        ])])

def toast():
    return html.Div([
        dbc.Toast(
                    "This file is in CSV format. To read it in Excel as a table, \
                    open a new Excel file, select the 'Data' Menu and then click on 'from text/CSV'.",
                    id="positioned-toast",
                    header="Downloading Data",
                    is_open=False,
                    dismissable=True,
                    icon="secondary",
                    # top: 66 positions the toast below the navbar
                    style={"position": "fixed", "top": 66, "right": 10, "width": 350},
                ),
            ])


def toast_spanish():
    return html.Div([
        dbc.Toast(
                    "Este archivo se encuentra en formato CSV. Para procesarlo en Excel como tabla, \
                    crea un nuevo documento Excel, selecciona el menú de 'Datos' y haz click en \
		    'Desde el texto/CSV'.",
                    id="positioned-toast",
                    header="Descargando Data",
                    is_open=False,
                    dismissable=True,
                    icon="secondary",
                    # top: 66 positions the toast below the navbar
                    style={"position": "fixed", "top": 66, "right": 10, "width": 350},
                ),
            ])

#Layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

english_page = html.Div([
    title.title(),
    tabs_layout(),
    toast()
], style={"padding": "0px 100px 0px 100px"})

page_1_layout = html.Div([
    title.title_spanish(),
    tabs_layout_spanish(),
    toast_spanish()
], style={"padding": "0px 100px 0px 100px"})

#Callbacks

## Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/spanish':
        return page_1_layout
    else:
        return english_page
    # You could also return a 404 "URL not found" page here

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
                  title="Ticker/Nemo: " + str(value).upper(),
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
     Input("ticker-dropdown", "value"),
     Input("roic-min", "value"),
     Input("roe-min", "value"),
     Input("op-margin-min", "value"),
     Input("hist-div-yield", "value"),
     Input("current-ratio-min", "value"),
     Input("current-ratio-max", "value")])
def update_table(page_current, page_size, sort_by, pe_min, pe_max, bv_min,
                 bv_max, filter_string, min_unint_div, ticker_dropdown,
                 roic_min, roe_min, op_margin_min, hist_div_yield_min,
                 current_ratio_min, current_ratio_max):

    # Filter

    max_unint_div = df["UNINT. DIV."].max()
    roic_max = df["ROIC (%)"].max()
    roe_max = df["ROE (%)"].max()
    op_margin_max = df["OP. MARGIN (%)"].max()
    hist_div_yield_max = df["HIST. DIV. YIELD (%)"].max()

    num_df = df[(df["PE"].between(pe_min, pe_max)) &
                (df["BV"].between(bv_min, bv_max)) &
                (df["UNINT. DIV."].between(min_unint_div, max_unint_div)) &
                (df["ROIC (%)"].between(roic_min, roic_max)) &
                (df["ROE (%)"].between(roe_min, roe_max)) &
                (df["OP. MARGIN (%)"].between(op_margin_min, op_margin_max)) &
                (df["HIST. DIV. YIELD (%)"].between(hist_div_yield_min, hist_div_yield_max)) &
                (df["CURRENT RATIO"].between(current_ratio_min, current_ratio_max))
                ] #to use OR, change "&" for "|"
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

#Value Collapse

@app.callback(
    Output("value-collapse", "is_open"),
    [Input("value-collapse-button", "n_clicks")],
    [State("value-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#Return Ratio Collapse

@app.callback(
    Output("return-ratio-collapse", "is_open"),
    [Input("return-ratio-collapse-button", "n_clicks")],
    [State("return-ratio-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#Financial Collapse

@app.callback(
    Output("financial-collapse", "is_open"),
    [Input("financial-collapse-button", "n_clicks")],
    [State("financial-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

#Download Data

@app.callback(
    Output('download-link', 'href'),
    [Input('datatable-paging', 'page_current'),
     Input('datatable-paging', 'page_size'),
     Input('datatable-paging', 'sort_by'),
     Input('pe-min', 'value'),
     Input("pe-max", "value"),
     Input("bv-min", "value"),
     Input("bv-max", "value"),
     Input("filter-input", "value"),
     Input("unint-div", "value"),
     Input("ticker-dropdown", "value"),
     Input("roic-min", "value"),
     Input("roe-min", "value"),
     Input("op-margin-min", "value"),
     Input("hist-div-yield", "value"),
     Input("current-ratio-min", "value"),
     Input("current-ratio-max", "value")])
def update_download_link(page_current, page_size, sort_by, pe_min, pe_max, bv_min,
                 bv_max, filter_string, min_unint_div, ticker_dropdown,
                 roic_min, roe_min, op_margin_min, hist_div_yield_min,
                 current_ratio_min, current_ratio_max):

    # Filter

    max_unint_div = df["UNINT. DIV."].max()
    roic_max = df["ROIC (%)"].max()
    roe_max = df["ROE (%)"].max()
    op_margin_max = df["OP. MARGIN (%)"].max()
    hist_div_yield_max = df["HIST. DIV. YIELD (%)"].max()

    num_df = df[(df["PE"].between(pe_min, pe_max)) &
                (df["BV"].between(bv_min, bv_max)) &
                (df["UNINT. DIV."].between(min_unint_div, max_unint_div)) &
                (df["ROIC (%)"].between(roic_min, roic_max)) &
                (df["ROE (%)"].between(roe_min, roe_max)) &
                (df["OP. MARGIN (%)"].between(op_margin_min, op_margin_max)) &
                (df["HIST. DIV. YIELD (%)"].between(hist_div_yield_min, hist_div_yield_max)) &
                (df["CURRENT RATIO"].between(current_ratio_min, current_ratio_max))
                ] #to use OR, change "&" for "|"
    final_df = num_df[num_df.apply(lambda row: row.str.contains(filter_string.upper(), regex=False).any(), axis=1)]

    if ticker_dropdown is None:
        filtered_df = final_df
    else:
        filtered_df = final_df[final_df["NEMO"].str.contains("|".join(ticker_dropdown))]
    
    csv_string = filtered_df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

#Toast

@app.callback(
    Output("positioned-toast", "is_open"),
    [Input("download-link", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False

#Main

if __name__ == '__main__':
    app.run_server(debug=True)
