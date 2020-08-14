import dash
import dash_core_components as dcc
import dash_html_components as html

def info():
    return html.Div([
    html.H2("What's New?"),
    dcc.Markdown("""
---

- 14/08/2020: Added the **Spanish version** with functionality.

- 13/08/2020: Improved the download link. You can now download the filtered data as you please.

- 12/08/2020: Improved code quality. Added "Download Data" button.

- 10/08/2020: Added new filters (ROIC, ROE, Op. Margin, Dividend Yield and Current Ratio)

- 9/08/2020: Improved UI

- 8/08/2020: Select your favorite stocks and compare!

- 7/08/2020: Added password protection and new columns for Stock Analysis section.

- 6/08/2020: Introducing, the **Orbis Academy!**

- 5/08/2020: Added **Price/Earning**, **Book Value**, and **Uninterrupted Dividend** filters to begin with your portfolio analysis.

- 4/08/2020: Added the **"Price" column** in the Stock Analysis section

- 2/08/2020: **Official release** of the Orbis Investments' SMW!""")])