import dash
import dash_core_components as dcc
import dash_html_components as html

def info():
    return html.Div([
    html.H2("What's New?"),
    dcc.Markdown("""
---

- 19/08/2020: Project complete. **Going live!**

- 16/08/2020: Completed the Spanish/English translation. Better mobile view.

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

def info_spanish():
    return html.Div([
    html.H2("Novedades"),
    dcc.Markdown("""
---

- 19/08/2020: Proyecto completado. **En vivo!**

- 16/08/2020: Fin de la traducción inglés/español. Se mejora la vista de celulares.

- 14/08/2020: **Sección en español** y funcional.

- 13/08/2020: Mejoras a la descarga de información, ahora se descarga la información filtrada.

- 12/08/2020: Mejoras en calidad de código. Se permite descargar información.

- 10/08/2020: Nuevos filtors (ROIC, ROE, Margen Op., Retorno de Dividendos y Test Líquido)

- 9/08/2020: Mejoras de UI

- 8/08/2020: Elija sus acciones favoritas y compare!

- 7/08/2020: Protección de contraseña y nuevas columnas en la sección de análisis.

- 6/08/2020: Bienvenidos a la **Academia Orbis!**

- 5/08/2020: Se agregaron los filtros para **Price/Earning**, **Book Value**, y **Dividendos Ininterrumpidos** para comenzar con el análisis de portafolio.

- 4/08/2020: Se agregó la columna de "Precio" en la sección de análisis

- 2/08/2020: **Publicación oficial** del Orbis Screener!""")])