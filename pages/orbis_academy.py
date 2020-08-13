import dash
import dash_core_components as dcc
import dash_html_components as html

##TAB 3

def info():
    return html.Div([
        html.H2("Orbis Academy"),
        dcc.Markdown("""
---
Here you will learn the most important  concepts to evaluate your investments and portfolios from a **value investing** standpoint."""),
        html.Table([
            html.Tr([html.Td(["Price/Earning Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The price-to-earnings ratio or P/E is one of the most widely-used stock analysis tools used by investors and analysts for determining stock valuation.
The P/E Ratio can be viewed sa the number of years it takes for the company to earn back the price you pay for the stock. Recommended P/E Ratio < 15.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            html.Tr([html.Td(["Book Value Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value.
It's calculated by dividing the company's stock price per share by its book value per share (BVPS).
An asset's book value is equal to its carrying value on the balance sheet, and companies calculate it netting the asset against its accumulated depreciation.
Recommended B/V < 2.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            html.Tr([html.Td(["Current Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The current ratio is a liquidity ratio that measures a company's ability to pay short-term obligations or those due within one year. Recommended ratio > 1.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})])
            ],
                   style={"width":"70%"})
        ])
