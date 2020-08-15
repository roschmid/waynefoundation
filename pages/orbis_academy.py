import dash
import dash_core_components as dcc
import dash_html_components as html

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
Recommended B/V < 2.5""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            
            html.Tr([html.Td(["Current Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The current ratio is a liquidity ratio that measures a company's ability to pay short-term obligations or those due within one year. Recommended ratio > 1.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Dividend Yield:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The dividend yield–displayed as a percentage–is the amount of money a company pays shareholders for owning a share of its stock divided by its current stock price.
In Chile, share companies are obliged to distribute at least 30% of their net income to shareholders as dividends. Recommended Dividend Yield > 5%""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Uninterrupted Dividend Distributions:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The uninterrupted dividend distributions column indicates the amount of years in a row a company has been distributing dividends. It is important to
bear in mind that companies with losses DO NOT distribute dividends. Thus, it is a good indicator if a company has been distributing for 5-10 years in a row, without interruptions.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Operating Margin:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The operating margin measures how much profit a company makes on a dollar of sales, after paying for variable costs of production, such as wages and
raw materials, but before paying interest or tax. It is calculated by dividing a company's operating profit by its net sales.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Return on Invested Capital (ROIC):"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Return on invested capital (ROIC) is a calculation used to assess a company's efficiency at allocating the capital under its control to profitable
investments. The return on invested capital ratio gives a sense of how well a company is using its money to generate returns.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),     
            
            ],
                   style={"width":"70%"})
        ])

def info_spanish():
    return html.Div([
        html.H2("Academia Orbis"),
        dcc.Markdown("""
---
Aquí aprenderás los conceptos más importantes para evaluar sus inversiones y carteras desde el punto de vista de la **inversión de valor**."""),
        html.Table([
            
            html.Tr([html.Td(["Price/Earning Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The price-to-earnings ratio or P/E is one of the most widely-used stock analysis tools used by investors and analysts for determining stock valuation.
The P/E Ratio can be viewed sa the number of years it takes for the company to earn back the price you pay for the stock. Recommended P/E Ratio < 15.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            
            html.Tr([html.Td(["Book Value Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value.
It's calculated by dividing the company's stock price per share by its book value per share (BVPS).
An asset's book value is equal to its carrying value on the balance sheet, and companies calculate it netting the asset against its accumulated depreciation.
Recommended B/V < 2.5""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            
            html.Tr([html.Td(["Current Ratio:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The current ratio is a liquidity ratio that measures a company's ability to pay short-term obligations or those due within one year. Recommended ratio > 1.5""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Dividend Yield:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The dividend yield–displayed as a percentage–is the amount of money a company pays shareholders for owning a share of its stock divided by its current stock price.
In Chile, share companies are obliged to distribute at least 30% of their net income to shareholders as dividends. Recommended Dividend Yield > 5%""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Uninterrupted Dividend Distributions:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The uninterrupted dividend distributions column indicates the amount of years in a row a company has been distributing dividends. It is important to
bear in mind that companies with losses DO NOT distribute dividends. Thus, it is a good indicator if a company has been distributing for 5-10 years in a row, without interruptions.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Operating Margin:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""The operating margin measures how much profit a company makes on a dollar of sales, after paying for variable costs of production, such as wages and
raw materials, but before paying interest or tax. It is calculated by dividing a company's operating profit by its net sales.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Return on Invested Capital (ROIC):"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Return on invested capital (ROIC) is a calculation used to assess a company's efficiency at allocating the capital under its control to profitable
investments. The return on invested capital ratio gives a sense of how well a company is using its money to generate returns.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),     
            
            ],
                   style={"width":"70%"})
        ])
