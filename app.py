# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Import libraries
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# "app" variable refers to the display
app = Dash()

# "df" variable refers to the DataFrame of daily_sales_data.csv
# contains "sales", "date", and "region"
df = pd.read_csv('data/daily_sales_data.csv')

# "fig" variable refers to the line chart
fig = px.line(df, x='date', y='sales', title='Sales by Date', color='region')

colors = {
    'background': '#0c1126',
    'plot': '#ffffff',
    'text': '#f5f4f0'
}

fig.update_layout(
    plot_bgcolor=colors['plot'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsels Sales by Date"),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run(debug=True)