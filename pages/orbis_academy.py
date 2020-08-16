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
            
            html.Tr([html.Td(["Razón Precio-Utilidad:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""La relación precio/beneficio o P/E es una de las herramientas de análisis de valores más utilizadas por los inversores y analistas para
determinar la valoración de acciones. La relación precio-beneficio o precio-utilidad puede verse como el número de años que le toma a la empresa recuperar el precio
que usted paga por la acción. Razón P/E recomendada < 15.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            
            html.Tr([html.Td(["Razón Precio-Valor Libros:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""Las empresas utilizan la relación precio-valor contable (relación P/B) para comparar la capitalización de mercado de una empresa con su
valor contable. Se calcula dividiendo el precio de las acciones de la empresa por su valor contable por acción (BVPS). El valor contable de un activo es igual a su valor
contable en el balance, y las empresas lo calculan compensando el activo con su depreciación acumulada. Recomendado B/V < 2.5""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),
            
            html.Tr([html.Td(["Test Líquido:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""El test líquido es un ratio de liquidez que mide la capacidad de una empresa para pagar las obligaciones a corto plazo o las que vencen en un año.
Ratio recomendado > 1.5""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Retorno de los Dividendos:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""El rendimiento de los dividendos -visualizado como un porcentaje- es la cantidad de dinero que una compañía paga a los accionistas por ser
propietaria de una parte de sus acciones dividida por su precio actual. En Chile, las sociedades anónimas están obligadas a distribuir al menos el 30% de sus ingresos netos
a los accionistas como dividendos. Rendimiento de Dividendos Recomendado > 5%""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Dividendos Ininterrumpidos:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""La columna de distribución ininterrumpida de dividendos indica la cantidad de años consecutivos en que una empresa ha estado distribuyendo
dividendos. Es importante tener en cuenta que las empresas con pérdidas NO distribuyen dividendos. Por lo tanto, es un buen indicador si una empresa ha estado distribuyendo
durante 5-10 años seguidos, sin interrupciones.""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Margen Operativo:"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""El margen de operación mide la cantidad de ganancias que una compañía obtiene con un dólar de ventas, después de pagar los costos variables
de producción, tales como salarios y materias primas, pero antes de pagar los intereses o impuestos. Se calcula dividiendo el beneficio de explotación de una empresa entre
sus ventas netas.""", style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),

            html.Tr([html.Td(["Retorno sobre el Capital Invertido (ROIC):"], style={"fontWeight": "bold", "borderBottom": "1px solid #ddd"}),
                     html.Td("""El retorno sobre el capital invertido (ROIC) es un cálculo utilizado para evaluar la eficiencia de una empresa en la asignación del capital
bajo su control a inversiones rentables. El índice de retorno del capital invertido da una idea de lo bien que una empresa está utilizando su dinero para generar retornos.""",
                             style={"borderBottom": "1px solid #ddd", "padding": "20px", "textAlign": "left"})]),     
            
            ],
                   style={"width":"70%"})
        ])
