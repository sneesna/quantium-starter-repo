# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Import libraries
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
from plotly.graph_objs.layout.scene import yaxis

# "app" variable refers to the display
app = Dash()

# "df" variable refers to the DataFrame of daily_sales_data.csv
# contains "sales", "date", and "region"
df = pd.read_csv('data/daily_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df['sales'] = df['sales'].str.replace(',','')
df['sales'] = df['sales'].str.replace('$', '')
df['sales'] = pd.to_numeric(df['sales'])

colors = {
    'background': '#0c1126',
    'otherBg': '#0e1730',
    'plot': '#f5f4f0',
    'primaryTxt': '#f5f4f0',
    'secondaryTxt': '#C3CED9',
    'tot_line': '#0c1126',
    'n_line': '#5B22E3',
    'e_line': '#078EE3',
    's_line': '#E39401',
    'w_line': '#E34707'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.Div(style={"height": "15px"}),

    # Title
    html.H1("Soul Foods Pink Morsels Sales by Date",
            style={'textAlign': 'center', 'color': colors['primaryTxt']}),

    # Configure Region and Year
    html.Div([

        html.H2("Configure Region",
                style={'textAlign': 'center', 'color': colors['primaryTxt']}),

        dcc.RadioItems(
            [
                {
                    'label': html.Div('All',
                        style={'color': colors['secondaryTxt']}),
                    'value': 'All'
                },
                {
                    'label': html.Div('North',
                        style={'color': colors['secondaryTxt']}),
                    'value': 'North'
                },
                {
                    'label': html.Div('East',
                        style={'color': colors['secondaryTxt']}),
                    'value': 'East'
                },
                {
                    'label': html.Div('South',
                        style={'color': colors['secondaryTxt']}),
                    'value': 'South'
                },
                {
                    'label': html.Div('West',
                        style={'color': colors['secondaryTxt']}),
                    'value': 'West'
                }
            ],
            'All', id='region-button', inline=True
        )],
        style={'width': '48%', 'display': 'inline-block',
               'textAlign': 'center'}
    ),

    html.Div([
        html.H2("Configure Year",
                style={'textAlign': 'center', 'color': colors['primaryTxt']}),

        dcc.RadioItems(
            [
                {
                    'label': html.Div('All',
                            style={'color': colors['secondaryTxt']}),
                    'value': 'All'
                },
                {
                    'label': html.Div('2018',
                            style={'color': colors['secondaryTxt']}),
                    'value': '2018'
                },
                {
                    'label': html.Div('2019',
                            style={'color': colors['secondaryTxt']}),
                    'value': '2019'
                },
                {
                    'label': html.Div('2020',
                            style={'color': colors['secondaryTxt']}),
                    'value': '2020'
                },
                {
                    'label': html.Div('2021',
                            style={'color': colors['secondaryTxt']}),
                    'value': '2021'
                },
                {
                    'label': html.Div('2022',
                            style={'color': colors['secondaryTxt']}),
                    'value': '2022'
                }],
            'All', id='year-button', inline=True
        )],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block',
               'textAlign': 'center'}
    ),

    html.Div(style={"height": "30px"}),

    dcc.Graph(
        id='sales-graph'
    ),

])

@callback(
    Output('sales-graph', 'figure'),
    Input('region-button', 'value'),
    Input('year-button', 'value')
)
def update_graph(region, year):
    this_radio = region.lower()
    if this_radio != 'all':
        dff = df[df['region'] == this_radio]
    else:
        dff = df

    if year != 'All':
        cur_yr = dff['date'].dt.year
        dfff = dff[cur_yr == int(year)]
    else:
        dfff = dff

    if str(region) == "All":
        my_color = colors['tot_line']
    elif str(region) == 'North':
        my_color = colors['n_line']
    elif str(region) == 'East':
        my_color = colors['e_line']
    elif str(region) == 'South':
        my_color = colors['s_line']
    else:
        my_color = colors['w_line']
    fig = px.line(dfff, x='date', y='sales', title='Sales by Date').update_traces(line_color=my_color)

    fig.update_layout(
        plot_bgcolor=colors['plot'],
        paper_bgcolor=colors['otherBg'],
        font_color=colors['primaryTxt'],
        yaxis=dict(
            title='Sales',
            tickprefix='$',
            ticksuffix='.00 ',
            tickformat=','
        ),
        xaxis=dict(
            title='Date',
            tickformat='%m/%d/20%y'
        )
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)