import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def title():
    return html.Div([
        dbc.Row([
            dbc.Col(html.H1("Orbis Investments Screener"), width=9),
            dbc.Col(dcc.Link("Español", href="/spanish"), width="auto"),
            dbc.Col(html.P("/"), width="auto"),
            dbc.Col(dcc.Link("English", href="/"), width="auto")]),
                     dcc.Markdown("---"),
                     dcc.Markdown("""
Welcome to the `Orbis Screener` ("OS"), created by Rafael Schmidt.\n
> **What is the OS?**\n
The OS is a place where you can analyze and prepare your personal portfolio
to invest in Chilean stocks.\n
Orbis Investments provides historical data on all of the stocks in the Chilean
market, such as price, dividend yield, PE ratio, among others.\n
Furthermore, you will be able to find information that is not
available even in the Chilean Stock Exchange.\n
For more information, do not hesitate to contact us via [GitHub](https://github.com/roschmid). \n
---
""")
                     ])

def title_spanish():
    return html.Div([
        dbc.Row([
            dbc.Col(html.H1("Orbis Investments Screener"), width=9),
            dbc.Col(dcc.Link("Español", href="/page-1"), width="auto"),
            dbc.Col(html.P("/"), width="auto"),
            dbc.Col(dcc.Link("English", href="/"), width="auto")]),
                     dcc.Markdown("---"),
                     dcc.Markdown("""
Bienvenido al `Orbis Screener` ("OS"), creado por Rafael Schmidt.\n
> **¿Qué es el OS?**\n
El OS es la herramienta que te permitirá analizar y preparar tu portafolio
personal para invertir en acciones chilenas.\n
Orbis Investments te provee información histórica de la totalidad de las
acciones del mercado chileno, tales como precio, retorno sobre dividendos,
razón precio-utilidad, entre otros.\n
Asimismo, podrás encontrar información valiosa que no se encuentra disponible en ninguna otra parte.\n
Para más información, no dudes en contactarnos vía [GitHub](https://github.com/roschmid). \n
---
""")
                     ])